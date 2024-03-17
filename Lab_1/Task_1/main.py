def hasExactChange(coinsBuyer, coinsSeller, targetAmount):
    if targetAmount == 0:
        return True

    if targetAmount < 0 or not coinsBuyer:
        return False

    currentCoin = coinsBuyer[0]
    remainingCoins = coinsBuyer[1:]

    if hasExactChange(coinsSeller, coinsSeller, targetAmount - currentCoin):
        return True

    if hasExactChange(remainingCoins, coinsSeller, targetAmount):
        return True

    return False

buyerCoins = [1, 2, 5]
sellerCoins = [1, 2, 5]
targetPrice = 3

if hasExactChange(buyerCoins, sellerCoins, targetPrice):
    print("Покупець може купити річ з точною здачею.")
else:
    print("Покупець не може купити річ з точною здачею.")
