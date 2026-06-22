import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor



# Part 1 fetch_posts

def fetch_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"შეცდომა User {user_id}-ის მონაცემების წამოღებისას: {e}")
    return []



# Part 2 count_posts

def count_posts(all_posts):
    counts = {}
    for post in all_posts:
        user_id = post['userId']
        counts[user_id] = counts.get(user_id, 0) + 1
    return counts


def find_longest_post(all_posts):
    if not all_posts:
        return None

    longest = max(all_posts, key=lambda post: len(post['body']))
    return {
        "userId": longest['userId'],
        "title": longest['title'],
        "length": len(longest['body'])
    }


def average_title_length(all_posts):
    if not all_posts:
        return 0.0

    total_length = sum(len(post['title']) for post in all_posts)
    return total_length / len(all_posts)

# Main

if __name__ == "__main__":
    user_ids = [1, 2, 3, 4, 5]

    print("მიმდინარეობს პოსტების ჩამოტვირთვა...")
    # 1. ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=5) as executor:

        downloaded_data = list(executor.map(fetch_posts, user_ids))

    all_posts = []
    for user_posts in downloaded_data:
        all_posts.extend(user_posts)

    if not all_posts:
        print("მონაცემების ჩამოტვირთვა ვერ მოხერხდა.")
        exit()

    print("მიმდინარეობს მონაცემების პარალელური დამუშავება...")
    # 2.ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(count_posts, all_posts)
        f2 = executor.submit(find_longest_post, all_posts)
        f3 = executor.submit(average_title_length, all_posts)

        post_counts = f1.result()
        longest_post = f2.result()
        avg_title_len = f3.result()

    # 3. Results
    print("\n" + "=" * 40)
    print(f"{'პოსტების ანალიზი':^40}")
    print("=" * 40)
    print(f"{'მომხმარებელი':<15}{'პოსტების რაოდენობა':<20}")
    print("-" * 40)

    for user_id in user_ids:
        count = post_counts.get(user_id, 0)
        print(f"User {user_id:<10}{count:<20}")

    print("\nყველაზე გრძელი პოსტი:")
    if longest_post:

        short_title = longest_post['title'][:40] + "..." if len(longest_post['title']) > 40 else longest_post['title']
        print(f"  მომხმარებელი: User {longest_post['userId']}")
        print(f"  სათაური: \"{short_title}\"")
        print(f"  სიგრძე: {longest_post['length']} სიმბოლო")
    else:
        print("  მონაცემები არ არის")

    print(f"\nსათაურების საშუალო სიგრძე: {avg_title_len:.1f} სიმბოლო")
    print("=" * 40)