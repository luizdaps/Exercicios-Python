larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
aréa = larg * alt
print('sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(larg, alt,aréa ))
tinta = aréa / 2
print('para pintar essa parede, vc precisará de {}l de tinta'.format(tinta))
