'''
Geometric progression
Get the estimated number if given a initial number and the multiplier over a sequence.
Use the formula for geometric progression: init_number * (multiplier ** num_of_items_in_seq -1)
assume no.of months already deducts 1 from itself.
'''

def geometric(follower_count, influencer_type, num_months):
    factor = 0
    if influencer_type == "fitness":
        factor = 4
    elif influencer_type == "cosmetic":
        factor = 3
    else: 
        factor = 2

    return follower_count * (factor ** num_months)