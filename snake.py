import pygame
class Snake:
    def __init__(self, screen):
        self.x = 50
        self.y = 0
        self.speed = 50
        self.image = pygame.image.load("Images/Snake.png")
        self.rect = self.image.get_rect()

        self.screen = screen
        self.dir = (1, 0)
        self.last_dir = self.dir
        self.frames = 0
        self.nextNode = None

    def move_me(self):
        self.frames += 1
        if self.frames == 20:
            self.frames = 0
            self.x += self.dir[0]*self.speed
            self.y += self.dir[1]*self.speed
            
            if self.nextNode != None:
                self.nextNode.dir = self.last_dir
            
            self.last_dir = self.dir
    
    def new_node(self):
        """ Creates a new node at the tail of the snake """
        currNode = self
        while currNode.nextNode != None:
            currNode = currNode.nextNode
        # Found the end
        newNode = Snake(currNode.screen)
        newNode.x = currNode.x + (50 * -currNode.dir[0])
        newNode.y = currNode.y + (50 * -currNode.dir[1])
        currNode.nextNode = newNode

    def move_body(self):
        bodyPart = self.nextNode
        while bodyPart != None:
            bodyPart.blit_me()
            bodyPart.move_me()
            bodyPart = bodyPart.nextNode

    def get_positions(self, includeHead = True):
        pos = []
        if includeHead:
            node = self
        else:
            node = self.nextNode
        while node != None:
            pos.append((node.x, node.y))
            node = node.nextNode
        
        return pos


    def check_loss(self):
        if (self.x, self.y) in self.get_positions(False):
            return True

        if self.x < 0 or self.x >= self.screen.get_rect().right:
            return True
        
        if self.y < 0 or self.y >= self.screen.get_rect().bottom:
            return True

    def blit_me(self):
        self.rect.x, self.rect.y = self.x, self.y
        self.screen.blit(self.image, self.rect)
