import platform
import user_agent
import fake_useragent

def get_platform_and_user_agent():
    # Get the platform information
    platform_info = platform.platform()

    # Get the user agent information
    ua_string = user_agent.generate_user_agent()

    return platform_info, ua_string

def set_custom_user_agent(custom_user_agent):
    # ua = UserAgent()
    # ua.update({'User-Agent': custom_user_agent})
    # return ua.random
    ua = fake_useragent.UserAgent(fallback='your favorite Browser')
    # ua.update({'User-Agent': 'blah'})
    # custom_ua_string = ua.random

    # in case if something went wrong, one more time it is REALLY!!! rare case
    ua.random == 'your favorite Browser'
    return ua.random

if __name__ == "__main__":
    platform_info, ua_string = get_platform_and_user_agent()
    print(f"Platform: {platform_info}")
    print(f"User Agent: {ua_string}")
    custom_ua = "My Custom User Agent"
    user_agent_string = set_custom_user_agent(custom_ua)
    print(f"Custom User Agent: {user_agent_string}")


    
    #approved platform    
    #voc-1092830982130812801283908123801028301928308912389021012830182308123001283081230120128301283081230812012893018230182
    