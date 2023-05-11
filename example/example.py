from hyparam import HyperParameters


def main():
    print("Hyper parameter usage example")

    # Define parameter space
    hp = HyperParameters()
    hp.add_linspace("learning_rate", 0.1, 0.3, 3)
    hp.add_switch("use_test_dataset")
    hp.add_range("epochs", 10, 30, 10)
    hp.add_list("myvar", [1.0, 12.0, 8.0])

    # Iterate over parameter space
    for choice in hp.choices():
        print(choice)
        # in real application, you implement a train(..) method that
        # trains your model given the hyper-parameter choices


if __name__ == "__main__":
    main()
