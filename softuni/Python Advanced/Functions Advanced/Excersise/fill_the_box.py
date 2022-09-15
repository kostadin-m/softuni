def fill_the_box(height,lenght,widht,*args):
    size_of_box = height * lenght * widht

    
    for i in range(args.index('Finish')):
            size_of_box -= args[i]

    if size_of_box < 0:
        return f'No more free space! You have {abs(size_of_box)} more cubes.'
    else:
        return f'There is free space in the box. You could put {size_of_box} more cubes.'

