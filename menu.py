import pygame
import sys

pygame.init()
pygame.display.set_caption("Monty's Hungry Python - Menu")
window = pygame.display.set_mode((720, 480))
font = pygame.font.SysFont('times new roman', 50)

def draw_menu():
    window.fill((0, 0, 0))
    title = font.render('Monty\'s Hungry Python', True, (255, 255, 255))
    play_text = font.render('Press Enter to Play', True, (0, 255, 0))
    quit_text = font.render('Press ESC to Quit', True, (255, 0, 0))
    
    title_rect = title.get_rect(center=(720 / 2, 100))
    play_rect = play_text.get_rect(center=(720 / 2, 250))
    quit_rect = quit_text.get_rect(center=(720 / 2, 350))
    
    window.blit(title, title_rect)
    window.blit(play_text, play_rect)
    window.blit(quit_text, quit_rect)
    pygame.display.update()

def main_menu():
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start game when Enter is pressed
                    import snake_game  # Import and run the main game
                    snake_game.main_game()  # Call main function from the main game file
                elif event.key == pygame.K_ESCAPE:  # Quit game when ESC is pressed
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()
