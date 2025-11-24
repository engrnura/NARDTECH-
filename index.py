"""import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import _cm
from ipython.display import HTML



def superficie_flor():
    [x, t] = np.meshgrid(np.array(range(25))/24.0, np.arange(0, 575.5, 0.5)/575*17*np.pi-2*np.pi)

    p = (np.pi/2)*np.exp(-t/(8*np.pi))
    u = 1-(1-np.mod(3.6*t, 2*np.pi)/np.pi)**4/2
    y = 2*(x**2-x)**2*np.sin(p)
    r = u*(x*np.sin(p)+y*np.cos(p))

    return r*np.cos(t), r*np.sin(t), u*(x*np.cos(p)-y*np.sin(p))

fig = plt.figure(figsize=(18, 18))
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("black")
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False


x, y, z =superficie_flor|()
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.gist_rainbow_r)


def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,

anim = animation.FuncAnimation(fig, 
                               animate, 
                               frames=360,
                               interval=20, 
                               blit=True)


anim.save("3D-flower.mp4", fps=30, extra_args=["-vcodec", "libx264"])

HTML(anim.to_html5_video())"""

class BankAccount:
    def init(self, name, number, balance, pin):
        self.name = name
        self.number = number
        self.balance = balance
        self.pin = pin
        self.is_active = True

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def deposit(self, amount):
        if not self.is_active:
            print("Account is closed.")
            return
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount, input_pin):
        if not self.is_active:
            print("Account is closed.")
            return
        if not self.verify_pin(input_pin):
            print("Incorrect PIN.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def check_balance(self, input_pin):
        if not self.verify_pin(input_pin):
            print("Incorrect PIN.")
            return
        print(f"Account balance: {self.balance}")

    def close_account(self, input_pin):
        if not self.verify_pin(input_pin):
            print("Incorrect PIN.")
            return
        self.is_active = False
        print("Account successfully closed.")

    def transfer(self, amount, recipient_account, input_pin):
        if not self.is_active:
            print("Account is closed.")
            return
        if not self.verify_pin(input_pin):
            print("Incorrect PIN.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        recipient_account.balance += amount
        print(f"Transfer successful! You sent {amount} to {recipient_account.name}.")


# Example Usage
acc1 = BankAccount()
#acc2 = BankAccount("Musa", 1002, 500, 2222)

"""acc1.deposit(200)
acc1.withdraw(300, 1234)
acc1.transfer(200, acc2, 1234)
acc1.check_balance(1234)"""