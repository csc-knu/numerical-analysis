#!/usr/bin/env python
import matplotlib.pyplot as plt
from dashpot import Dashpot
from car import Car
from road import Road
from stage import Stage


def splot(save=False):
    if save:
        plt.figure(figsize=(20,10))

    plt.xlabel('$t$', fontsize=16)


def fplot(save=False):
    global _IMG
    _IMG += 1
    plt.legend(fontsize=16)
    plt.grid(True)
        
    if save:
        plt.savefig(f'../tex/{_IMG}.png', bbox_inches='tight')
    else:
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()


if __name__ == '__main__':
    _IMG = 0
    T_MAX = 5 + 1e-7
    h_t, h_x, h_x_0, h_dot_x, h_xi = [], [], [], [], []
    dt = .0001
    stage = Stage(
        car=Car(m=10, dashpot=Dashpot(k=640, r_0=160, c=1)), 
        road=Road(a=2, omega=7)
    )

    while stage.t <= T_MAX:
        h_t.append(stage.t)
        h_x.append(stage.x)
        h_x_0.append(stage.x_0)
        h_dot_x.append(stage.dot_x)
        h_xi.append(stage.xi)
        print(stage)
        stage.move(dt)

    splot(save=False)
    plt.title(
        f'Solution plot with Runge-Kutta on $[{h_t[0]:.2f}, {h_t[-1]:.2f}]$\n'
        f'$x(0) = {h_x[0]:.2f}, \\dot x(0) = {h_dot_x[0]:.2f}$', fontsize=20
    )
    plt.ylabel('$x(t), \\dot x(t)$', fontsize=16)
    plt.plot(h_t, h_x, 'r-', label='$x(t)$')
    plt.plot(h_t, h_dot_x, 'b-', label='$\\dot x(t)$')
    fplot(save=False)

    splot(save=False)
    plt.title(
        f'Solution plot with Runge-Kutta on $[{h_t[0]:.2f}, {h_t[-1]:.2f}]$\n'
        f'$x(0) = {h_x[0]:.2f}, \\dot x(0) = {h_dot_x[0]:.2f}$', fontsize=20
    )
    plt.ylabel('$x(t), x_0(t)$', fontsize=16)
    plt.plot(h_t, h_x, 'r-', label='$x(t)$')
    plt.plot(h_t, h_x_0, 'b-', label='$x_0(t)$')
    fplot(save=False)

    splot(save=False)
    plt.title(
        f'Dashpot influence with Runge-Kutta on $[{h_t[0]:.2f}, {h_t[-1]:.2f}]$\n'
        f'$x(0) = {h_x[0]:.2f}, \\dot x(0) = {h_dot_x[0]:.2f}$', fontsize=20
    )
    plt.ylabel('$x(t) - x_0(t)$', fontsize=16)
    plt.plot(h_t, [h_x[i] - h_x_0[i] for i in range(len(h_t))], 
        'g-', label='$x(t) - x_0(t)$')
    fplot(save=False)

    splot(save=False)
    plt.title(
        f'Dashpot load with Runge-Kutta on $[{h_t[0]:.2f}, {h_t[-1]:.2f}]$\n'
        f'$x(0) = {h_x[0]:.2f}, \\dot x(0) = {h_dot_x[0]:.2f}$', fontsize=20
    )
    plt.ylabel('$\\xi(t)$', fontsize=16)
    plt.plot(h_t, h_xi, 'g-', label='$\\xi(t)$')
    fplot(save=False)
