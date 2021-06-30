import generator

generator.logging.info('Package __init__ executed.')
for x in range(5):
    generator.logging.info('[Name chosen.]')
    generator.logging.info('[Title chosen.]')
    generator.logging.info(f'Sir {generator.names.names()} the {generator.titles.titles()}')
