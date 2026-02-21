'''
return the sum of items where brand_name is present per influencers
Send the average

O(nm)
'''

def get_avg_brand_followers(all_handles, brand_name):
    found = 0
    influencers = len(all_handles)
    for influencer in all_handles:
        for handle in influencer:
            if handle.find(brand_name) != -1:
                found += 1

    return found/influencers