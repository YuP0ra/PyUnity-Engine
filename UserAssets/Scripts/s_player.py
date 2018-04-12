from UserAssets.Scripts.basics import *

player = Animation('player.png', 27, 2)
transform = Transform2D()
collider = BoxCollider2D(5, 5, transform)

speed = Vector3(0, 0, 0)
__id__ = 'player'
animate = True


def Render():
    collider.render()

    # must add
    transform.applyTransformation()

    # your render code here
    player.render(animate=animate)


def Start():
    transform.scale = Vector3(2, 2, 2)
    transform.position.z = -1
    collider.on_collision_trigger(oncoll)


def Update():
    global speed, animate

    animate = False

    if Input.KeyHold('d'):
        transform.position += transform.right * Time.deltaTime * 5
        transform.scale.x = +2
        animate = True

    if Input.KeyHold('a'):
        transform.position -= transform.right * Time.deltaTime * 5
        transform.scale.x = -2
        animate = True

    if Input.KeyHold(' '):
        speed = Vector3(0, 10, 0)

    transform.position += speed * Time.deltaTime

    if transform.position.y <= -1:
        speed = Vector3(0, 0, 0)
    else:
        speed += Vector3(0, -1, 0) * 30 * Time.deltaTime


def oncoll(hits):
    global speed
    for hit in hits:
        if hit == 'bullet':
            speed = Vector3(0, 10, 0)