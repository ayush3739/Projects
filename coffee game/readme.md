# Coffee Machine Simulator

A sophisticated coffee machine simulator with inventory management, payment processing, and multiple drink options.

## Features
- Multiple coffee drink options (espresso, latte, cappuccino)
- Resource management (water, milk, coffee beans)
- Coin-based payment system
- Change calculation and return
- Inventory tracking and reports
- Machine maintenance functions

## Game Components
- `main.py` - Main machine controller and user interface
- `menu.py` - Drink menu and pricing system
- `coffee_maker.py` - Coffee brewing and resource management
- `money_machine.py` - Payment processing and change handling

## Available Commands
- **Drink names** (espresso/latte/cappuccino) - Order a drink
- **"report"** - View current resource levels and money
- **"off"** - Turn off the machine (admin command)

## How It Works
1. User selects a drink from the available menu
2. Machine checks if sufficient resources are available
3. User inserts coins (quarters, dimes, nickels, pennies)
4. Machine processes payment and calculates change
5. If successful, coffee is brewed and resources are deducted
6. Transaction is completed with change returned if applicable

## Drink Menu
- **Espresso**: $1.50 (50ml water, 18g coffee)
- **Latte**: $2.50 (200ml water, 150ml milk, 24g coffee)
- **Cappuccino**: $3.00 (250ml water, 100ml milk, 24g coffee)

## Machine Management
- Automatic resource tracking
- Low resource warnings
- Daily sales reporting
- Maintenance alerts

## Example Usage
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.00 in change.
Here is your latte ☕ Enjoy!
```

## Learning Concepts
- Object-oriented programming
- Class interaction and composition
- Resource management systems
- Financial transaction processing
- User interface design
- Error handling and validation

## Requirements
- Python 3.x
- No external dependencies required

## Admin Features
- View resource reports
- Monitor profit and sales
- Machine shutdown capability