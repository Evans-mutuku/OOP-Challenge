from pet import Pet

def main():
    buddy = Pet("Barnabu")

    buddy.get_status()
    buddy.eat()
    buddy.play()
    buddy.sleep()
    buddy.train("roll over")
    buddy.train("fetch")
    buddy.show_tricks()
    buddy.get_status()

if __name__ == "__main__":
    main()
