#%%
def initialize():
    global health, hedons, cur_star, cur_time, star_history, bored
    global run_expiry_time, tired_expiry_time

    health = 0
    hedons = 0
    cur_star = ''
    cur_time = 0

    star_history = []
    bored = False
    run_expiry_time = 180
    tired_expiry_time = 0


def get_cur_hedons():
    return hedons


def get_cur_health():
    return health


def perform_activity(activity, duration):
    global health, hedons, cur_star, cur_time
    global run_expiry_time, tired_expiry_time

    health += calc_health_gained(activity, duration)
    hedons += calc_hedons_gained(activity, duration)

    if activity == 'running':
        run_expiry_time -= duration
        if run_expiry_time <= 0:
            run_expiry_time = 0
        tired_expiry_time = 120
    elif activity == 'textbooks':
        run_expiry_time = 180
        tired_expiry_time = 120
    elif activity == 'resting':
        run_expiry_time = 180
        tired_expiry_time -= duration
    else:
        pass
    
    cur_time += duration
    cur_star = ''

    return None


def calc_health_gained(activity, duration):
    global run_expiry_time

    if activity == 'running':
        if duration < run_expiry_time:
            health_gained = duration * 3
        else:
            health_gained = (run_expiry_time * 3) + (duration - run_expiry_time)

    elif activity == 'textbooks':
        health_gained = 2 * duration

    else:
        health_gained = 0
    return health_gained


def calc_hedons_gained(activity, duration):
    global tired_expiry_time, cur_star

    # calculate hedon increase RATE
    if activity == 'running':
        if tired_expiry_time > 0:
            hedons_incr_rate = -2
        else:
            hedons_incr_rate = 2
            max_hedon_time = 10
    elif activity == 'textbooks':
        if tired_expiry_time > 0:
            hedons_incr_rate = -2
        else:
            hedons_incr_rate = 1
            max_hedon_time = 20
    else:
        hedons_incr_rate = 0
        max_hedon_time = 0

    # calculate hedons gained
    if tired_expiry_time > 0:
        hedons_gained = hedons_incr_rate * duration
    else:
        hedons_gained = (hedons_incr_rate * max_hedon_time) - (abs(duration - max_hedon_time) * hedons_incr_rate)
    
    # accounting for stars
    if activity == cur_star:
        hedons_gained += min(duration, 10) * 3

    return hedons_gained


def offer_star(activity):
    '''Offers star to user engaging in activity'''
    global cur_time, cur_star, star_history, bored

    star_history.append(cur_time)
    if len(star_history) > 3:
        star_history = star_history[1:]
    if (len(star_history) == 3) and (cur_time - star_history[0] < 120):
        bored = True
    if not bored:
        cur_star = activity
    return


def star_can_be_taken(activity):
    '''Return True if star can be used for specified activity.'''
    return activity == cur_star


def most_fun_activity_minute():
    '''Returns activity which would give most hedons
     if performed for one minute at current time'''
    max_hedons = 0
    for activity in ['running', 'textbooks', 'resting']:
        compare_hedons = calc_hedons_gained(activity, 1)
        if compare_hedons >= max_hedons:
            max_hedons = compare_hedons
            most_fun_activity = activity
    return most_fun_activity






if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            #-20 = 10 * 2 + 20 * (-2)
    print(get_cur_health())            #90 = 30 * 3
    print(most_fun_activity_minute())  #resting
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  #running
    perform_activity("textbooks", 30)  
    print(get_cur_health())            #150 = 90 + 30*2
    print(get_cur_hedons())            #-80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            #210 = 150 + 20 * 3
    print(get_cur_hedons())            #-90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())            #700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())            #-430 = -90 + 170 * (-2)
# %%
