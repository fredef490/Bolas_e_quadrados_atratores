class Retangulo:
    def __init__(self, x, y, tamx, tamy):
        rectMode(CENTER)
        self.x = x
        self.y = y
        self.tamx = random(5, 50)
        self.tamy = random(5, 50)
        self.cor = color(random(255),
                         random(255),
                         random(255))
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
        
    def plot(self):
        rect(self.x, self.y, self.tamx, self.tamy)
        fill(color(self.cor))
        noStroke()
        
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x > width or self.x < 0:
            self.vx = -self.vx
        if self.y > height or self.y < 0:
            self.vy = -self.vy
        print(self.vx, self.vy)

    def velocidade_pos(self):
        if self.vx > 0 and self.vy > 0:
            self.vx, self.vy = self.vx +1, self.vy +1
        if self.vx < 0 and self.vy < 0:
            self.vx, self.vy = self.vx -1, self.vy -1
        if self.vx > 0 and self.vy < 0:
            self.vx, self.vy = self.vx +1, self.vy -1
        if self.vx < 0 and self.vy > 0:
            self.vx, self.vy = self.vx -1, self.vy +1
    
    def velocidade_neg(self):
        if self.vx > 0 and self.vy > 0:
            self.vx, self.vy = self.vx -1, self.vy -1
        if self.vx < 0 and self.vy < 0:
            self.vx, self.vy = self.vx +1, self.vy +1
        if self.vx > 0 and self.vy < 0:
            self.vx, self.vy = self.vx -1, self.vy +1
        if self.vx < 0 and self.vy > 0:
            self.vx, self.vy = self.vx +1, self.vy -1
    
    def direcao(self):  
        if self.x > mouseX or self.x < mouseX:
            self.vx = -1 * (self.x - mouseX) / 50
        if self.y > mouseY or self.x < mouseY:
            self.vy = -1 * (self.y - mouseY) / 50
    
    def direcao2(self):
        if self.x > mouseX or self.x < mouseX:
            self.vx = (self.x - mouseX) / 50
        if self.y > mouseY or self.x < mouseY:
            self.vy = (self.y - mouseY) / 50
