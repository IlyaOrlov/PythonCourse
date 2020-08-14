def always_best_review(review):
    dict_review = {"долго": "быстро",
                   "редиска": "замечательный человек",
                   "низкого качества": "наилучшего качества",
                   "не ": ""}

    for key, value in dict_review.items():
        review = review.replace(key, value)

    print("Good review is done:")
    print(review)


bad_review = "Заказ шёл долго. Товар низкого качества не порадовал. Продавец - редиска. Заказывать больше не буду!"
print(bad_review)
always_best_review(bad_review)
