import random

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce(self, ball):
        if self.collide_widget(ball):
            # vx, vy = ball.velocity
            # bounced_vel = Vector(-1 * vx, vy)
            # bounced_vel *= 1.5
            # ball.velocity = bounced_vel

            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGameWidget(Widget):
    ball = ObjectProperty(None)
    left_paddle = ObjectProperty(None)
    right_paddle = ObjectProperty(None)

    def serve_ball(self):

        self.ball.center = self.center
        vel = 0
        rand = random.choice([0,1])
        if rand == 1:
            vel = (4, 0)
        else:
            vel = (-4, 0)
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.right_paddle.bounce(self.ball)
        self.left_paddle.bounce(self.ball)

        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.left_paddle.score += 1
            self.serve_ball()
        elif self.ball.x > self.width:
            self.right_paddle.score += 1
            self.serve_ball()

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.left_paddle.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.right_paddle.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGameWidget()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60)
        return game

