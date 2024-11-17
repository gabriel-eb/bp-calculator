from enum import Enum

class Routes(Enum):
    DERIVATIVE = 'derivative'
    INTEGRAL = 'integral'
    FINITE = 'finite-sum'
    INFINITE = 'infinite-sum'
    MAINMENU = 'main-menu'
    OPERATION = 'operation'
    
calc_options = [
    Routes.DERIVATIVE.value,
    Routes.INTEGRAL.value,
    Routes.FINITE.value,
    Routes.INFINITE.value,
]