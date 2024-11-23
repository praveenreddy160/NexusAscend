import requests
from bs4 import BeautifulSoup

def get_follower_count(name):
  """
  getting the follower count
  """
  query = f"{name} followers"
  url = f"https://www.google.com/search?q={query}"
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  }

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # This part might need adjustments depending on Google's search result layout
    follower_count_element = soup.find("div", class_="BNeawe iBp4i AP7Wnd") 
    if follower_count_element:
      follower_count_text = follower_count_element.get_text()
      # Extract the numeric part (this might need refinement for different formats)
      follower_count = int("".join(filter(str.isdigit, follower_count_text)))
      return follower_count

  except requests.exceptions.RequestException as e:
    print(f"Error fetching search results: {e}")
  except Exception as e:
    print(f"Error extracting follower count: {e}")

  return None

def higher_lower_followers():
  """Plays the Higher Lower game based on follower counts."""

  score = 0
  playing = True

  while playing:
    person1 = input("Enter the name of the first person:\n ")
    person2 = input("Enter the name of the second person:\n")

    followers1 = get_follower_count(person1)
    followers2 = get_follower_count(person2)

    if followers1 is None or followers2 is None:
      print("Could not find follower information for one or both people. Try again.")
      continue

    print(f"\nWho has more followers?")
    print(f"1. {person1}")
    print(f"2. {person2}")
    guess = input("Enter your choice (1 or 2) or 'q' to quit: ").lower()

    if guess == 'q':
      playing = False
    elif (guess == '1' and followers1 > followers2) or \
         (guess == '2' and followers2 > followers1):
      score += 1
      print("Correct!")
    else:
      print("Incorrect!")
      print(f"{person1} has approximately {followers1} followers.")
      print(f"{person2} has approximately {followers2} followers.")

  print(f"\nGame over! Your final score is {score}")

if __name__ == "__main__":
  higher_lower_followers()