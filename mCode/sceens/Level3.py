import math
import random

import pygame, sys, time
from random import choice, randint

from pygame import Vector2

from mCode.sceens.Game import Game
from mCode.settings import UPGRADES, BLOCK_MAP, BLOCK_WIDTH, GAP_SIZE, BLOCK_HEIGHT, TOP_OFFSET
from mCode.sprites import Player, Ball, Upgrade, Block, Projectile
from mCode.surfacemaker import SurfaceMaker
from mCode.utils.util import utils


class Level3(Game):
    def __init__(self,score = 0):
        # general setup
        # background
        self.bg = self.create_bg()

        # sprite group setup
        self.all_sprites = pygame.sprite.Group()
        self.block_sprites = pygame.sprite.Group()
        self.upgrade_sprites = pygame.sprite.Group()
        self.projectile_sprites = pygame.sprite.Group()

        # setup
        self.surfacemaker = SurfaceMaker()
        self.player = Player(self.all_sprites, self.surfacemaker)
        self.stage_setup((100,100))
        self.stage_setup((700,100))
        self.ball = Ball(self.all_sprites, self.player, self.block_sprites)

        # hearts
        self.heart_surf = pygame.image.load('../graphics/other/heart.png').convert_alpha()

        # projectile
        self.projectile_surf = pygame.image.load('../graphics/other/projectile.png').convert_alpha()
        self.can_shoot = True
        self.shoot_time = 0

        # crt
        self.crt = CRT()

        self.laser_sound = pygame.mixer.Sound('../sounds/laser.wav')
        self.laser_sound.set_volume(0.1)

        self.powerup_sound = pygame.mixer.Sound('../sounds/powerup.wav')
        self.powerup_sound.set_volume(0.1)

        self.laserhit_sound = pygame.mixer.Sound('../sounds/laser_hit.wav')
        self.laserhit_sound.set_volume(0.02)

        self.music = pygame.mixer.Sound('../sounds/music.wav')
        self.music.set_volume(0.1)
        self.music.play(loops=-1)
        self.score = score

    def create_upgrade(self, pos):
        upgrade_type = choice(UPGRADES)
        Upgrade(pos, upgrade_type, [self.all_sprites, self.upgrade_sprites])

    def create_bg(self):
        bg_original = pygame.image.load('../graphics/other/bg.png').convert()
        scale_factor = utils.height / bg_original.get_height()
        scaled_width = bg_original.get_width() * scale_factor
        scaled_height = bg_original.get_height() * scale_factor
        scaled_bg = pygame.transform.scale(bg_original, (scaled_width, scaled_height))
        return scaled_bg

    def stage_setup(self,start_pos):
        # Define square parameters
        square_size = 300  # Length of one side of the square
        start_pos =start_pos
        num_blocks = sum(len(row) for row in BLOCK_MAP if row.strip())  # Total number of blocks

        # Blocks per side
        blocks_per_side = num_blocks // 4
        extra_blocks = num_blocks % 4  # In case the blocks don't divide evenly

        block_index = 0  # To track block placement
        side_lengths = [blocks_per_side] * 4  # Equal distribution
        for i in range(extra_blocks):
            side_lengths[i] += 1  # Distribute extra blocks

        for side, side_length in enumerate(side_lengths):
            for i in range(side_length):
                if block_index < num_blocks:
                    # Calculate position based on the side
                    if side == 0:  # Top side
                        x = start_pos[0] + i * (square_size // side_length)
                        y = start_pos[1]
                    elif side == 1:  # Right side
                        x = start_pos[0] + square_size
                        y = start_pos[1] + i * (square_size // side_length)
                    elif side == 2:  # Bottom side
                        x = start_pos[0] + square_size - i * (square_size // side_length)
                        y = start_pos[1] + square_size
                    elif side == 3:  # Left side
                        x = start_pos[0]
                        y = start_pos[1] + square_size - i * (square_size // side_length)

                    # Create block
                    Block(random.choice(['2','3','4','5']), (x, y), [self.all_sprites, self.block_sprites], self.surfacemaker, self.create_upgrade)
                    block_index += 1

    def display_hearts(self):
        for i in range(self.player.hearts):
            x = 2 + i * (self.heart_surf.get_width() + 2)
            utils.screen.blit(self.heart_surf, (x, 4))

    def upgrade_collision(self):
        overlap_sprites = pygame.sprite.spritecollide(self.player, self.upgrade_sprites, True)
        for sprite in overlap_sprites:
            self.player.upgrade(sprite.upgrade_type)
            self.powerup_sound.play()

    def create_projectile(self):
        self.laser_sound.play()
        for projectile in self.player.laser_rects:
            Projectile(
                projectile.midtop - pygame.math.Vector2(0, 30),
                self.projectile_surf,
                [self.all_sprites, self.projectile_sprites])

    def laser_timer(self):
        if pygame.time.get_ticks() - self.shoot_time >= 500:
            self.can_shoot = True

    def projectile_block_collision(self):
        for projectile in self.projectile_sprites:
            overlap_sprites = pygame.sprite.spritecollide(projectile, self.block_sprites, False)
            if overlap_sprites:
                for sprite in overlap_sprites:
                    sprite.get_damage(1)
                    self.score += 1
                    if sprite.health <= 0:
                        self.score += 10
                projectile.kill()
                self.laserhit_sound.play()

    def onKeyDown(self, key):
            if key == pygame.K_SPACE:
                self.ball.active = True
                if self.can_shoot:
                    self.create_projectile()
                    self.can_shoot = False
                    self.shoot_time = pygame.time.get_ticks()

    def update(self):
        if self.player.hearts <= 0:
            from mCode.sceens.GameOver import GameOver
            utils.currentScreen = GameOver(self.score)

        if self.countBlock() <= 0:
            from mCode.sceens.YouWin import YouWin
            utils.currentScreen = YouWin(self.score)

        # draw bg
        utils.screen.blit(self.bg, (0, 0))

        # update the game
        self.all_sprites.update(utils.deltaTime())
        self.upgrade_collision()
        self.laser_timer()
        self.projectile_block_collision()

        # draw the frame
        self.all_sprites.draw(utils.screen)
        self.display_hearts()

        # crt styling
        self.crt.draw()

        text = "score: " + str(self.score)
        tw = utils.font32.render(text, True, (0, 0, 0)).get_width()
        utils.drawText(Vector2(1000,2), text, (255, 255, 255), utils.font18)

        text = "level: 2"
        utils.drawText(Vector2(300, 2), text, (255, 255, 255), utils.font18)

        # update window
        pygame.display.update()

    def countBlock(self):
        return len(self.block_sprites)

    def draw(self):
        pass

class CRT:
    def __init__(self):
        vignette = pygame.image.load('../graphics/other/tv.png').convert_alpha()
        self.scaled_vignette = pygame.transform.scale(vignette, (utils.width, utils.height))
        utils.screen = pygame.display.get_surface()
        self.create_crt_lines()

    def create_crt_lines(self):
        line_height = 4
        line_amount = utils.height // line_height
        for line in range(line_amount):
            y = line * line_height
            pygame.draw.line(self.scaled_vignette, (20, 20, 20), (0, y), (utils.width, y), 1)

    def draw(self):
        self.scaled_vignette.set_alpha(randint(60, 75))
        utils.screen.blit(self.scaled_vignette, (0, 0))
