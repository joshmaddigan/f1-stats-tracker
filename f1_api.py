import fastf1

def get_session(year, gp, session):
       # Load the session data
    fastf1.Cache.enable_cache('cache')  # Enable caching to speed up future requests
    session_data = fastf1.get_session(year, gp, session)
    
    # Load the session data into memory
    session_data.load()
    # print(session_data.results.columns.tolist())
    
    return session_data 

# Example usage
if __name__ == "__main__":   
    session = get_session(2024, 'Italian', 'R')