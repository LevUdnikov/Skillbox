# Папа-программист уже настолько обленился,
# что вместо того, чтобы самому спросить у сына, какую оценку тот получил в школе,
# он написал для этого вот такую программу:

rating = int(input('Что получил по математике? '))
if rating == (2 or 3):
    print('Плохо. Марш учиться!')

if rating == 4:
    print('Молодец! Можешь отдохнуть.')
if rating == 5:
    print('Молодец! Можешь отдохнуть.')

# Сын после того, как «сообщил» свою оценку, посмотрел на код программы и понял,
# что её можно улучшить, и даже рассказал папе, как это сделать,
# за что получил безграничное уважение от отца.

# 1) При плохой оценке (2 или 3) выводится сообщение: «Плохо. Марш учиться!».
# 2) При хорошей оценке (4 или 5) выводится сообщение: «Молодец! Можешь отдохнуть».
# 3) В программе не должно быть повторяющихся строк.