celcius = float(input('Informe a temperatura em °C: '))

fahrenheit = celcius * 1.8 + 32

print(
    'A temperatura de {:.1f}°C '
    'corresponde a {:.1f}°F'
    .format(
        celcius,
        fahrenheit
    )
)