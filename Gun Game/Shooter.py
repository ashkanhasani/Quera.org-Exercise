class Gun:
    def __init__(self, name, range_shoot, power, bullet_size):
        self.range_shoot = range_shoot
        self.power = power
        self.bullet_size = bullet_size
        self.name = name


class Bullet:
    def __init__(self, name, size, hurt):
        self.name = name
        self.size = size
        self.hurt = hurt


class Shooter:
    def __init__(self):
        self.gun = None
        self.bullet = None
        self.bullet_count = 0

    def set_gun_by_name(self, name: str) -> None:
        if name == "Submachine Gun":
            self.gun = Gun("submachine Gun", 100, 10, 0.5)
        elif name == "Assault Rifle":
            self.gun = Gun("Assault Rifle", 200, 20, 1)
        elif name == "Pistol":
            self.gun = Gun("Pistol", 80, 8, 0.5)
        elif name == "Shotgun":
            self.gun = Gun("Shotgun", 50, 40, 4)
        elif name == "Sniper Rifle":
            self.gun = Gun("Sniper Rifle", 1000, 30, 3)
        else:
            raise Exception("your gun does not exist")

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        if size == 0.5:
            self.bullet = Bullet("A", 0.5, 1)
        elif size == 1:
            self.bullet = Bullet("B", 1, 1.5)
        elif size == 3:
            self.bullet = Bullet("C", 3, 3)
        elif size == 4:
            self.bullet = Bullet("D", 4, 2)
        else:
            raise Exception("you dont have bullets with this size")
        if not self.gun or self.gun.bullet_size != size:
            raise Exception
        if count < 0:
            raise Exception
        else:
            self.bullet_count = count

    def shoot_to_target(self, target_x: int, target_y: int, target_distance: int, aim_x: int, aim_y: int) -> float:
        if not self.gun or not self.bullet:
            raise Exception
        elif self.bullet_count == 0:
            raise Exception
        else:
            if target_distance <= self.gun.range_shoot:
                return self.gun.power * self.bullet.hurt
            else:
                return 0


