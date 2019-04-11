import arrow

t0 = arrow.now()
print(t0)

t1 = arrow.utcnow()
print(t1)

difference = (t0 - t1).total_seconds()

print('Total difference: %.2f seconds ' % difference)
print(f'Humanized: {t0.humanize()}')
print(f'Humanized: {t0.humanize(locale="es")}')
print(f'Humanized: {t0.humanize(locale="ja")}')

t0 = t0.replace(hours=-3, minutes=10)
print(f'Humanized: {t0.humanize()}')