def movement(obj, direction, speed, camera):
    # use camera to check padding
    # if direction == 'right':
    #     if obj.rect.x < camera.rect.x + camera.rect.width - obj.rect.width - camera.padding:
    #         obj.rect.x += speed
    #         obj.direction = 'right'
    # elif direction == 'left':
    #     if obj.rect.x > camera.rect.x + camera.padding:
    #         obj.rect.x -= speed
    #         obj.direction = 'left'
    # elif direction == 'up':
    #     if obj.rect.y > camera.rect.y + camera.padding:
    #         obj.rect.y -= speed
    #         obj.direction = 'up'
    # elif direction == 'down':
    #     if obj.rect.y < camera.rect.y + camera.rect.height - obj.rect.height - camera.padding:
    #         obj.rect.y += speed
    #         obj.direction = 'down'

    if direction == 'right':
        obj.rect.x += speed
    elif direction == 'left':
        obj.rect.x -= speed
    elif direction == 'up':
        obj.rect.y -= speed
    elif direction == 'down':
        obj.rect.y += speed
