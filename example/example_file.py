from hyparam import HyperParameters


def main():
    print("Hyper parameter usage example")

    # Define parameter space
    hp = HyperParameters.from_file("config.yaml")

    # Iterate over parameter space
    for choice in hp.choices():
        print(choice)
        # in real application, you implement a train(..) method that
        # trains your model given the hyper-parameter choices


if __name__ == "__main__":
    main()
