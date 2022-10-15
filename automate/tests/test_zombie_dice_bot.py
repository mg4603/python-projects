from scripts.zombie_dice_bot import MyZombie

def test_MyZombie():
    zombie = MyZombie("lol")
    assert zombie.name == 'lol'