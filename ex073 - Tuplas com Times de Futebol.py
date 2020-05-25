teams = (
    'Flamengo',
    'Santos',
    'Palmeiras',
    'Grêmio',
    'Athletico-PR',
    'São Paulo',
    'Internacional',
    'Corinthians',
    'Fortaleza',
    'Goiás',
    'Bahia',
    'Vasco da Gama',
    'Atlético-MG',
    'Fluminense',
    'Botafogo',
    'Ceará',
    'Cruzeiro',
    'CSA',
    'Chapecoense',
    'Avaí'
)

print('=-' * 15)
print(f'Lista de times do Brasileirão 2019: {teams}')
print('=-' * 15)
print(f'Os cinco primeiros são: {teams[:5]}')
print('=-' * 15)
print(f'Os 4 últmos são: {teams[-4:]}')
print('=-' * 15)
print(f'Times em ordem alfabetica: {sorted(teams)}')
print('=-' * 15)
print(f'O Chapecoense está na {teams.index("Chapecoense") + 1}ª posição')
