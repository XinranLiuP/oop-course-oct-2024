# OOP Exercises

This week's exercises will guide you through a mock implementation of a basic backend for online marketplaces.
In tackling the exercises, you might wish to follow the specifications given in the [Assignment Example](./ASSIGNMENT.md).

You should read the [Specification](#specification) and then proceed to follow the steps listed under [Implementation](#implementation).
The afternoons Tue-Thu 2pm-5pm will be dedicated to the exercises, so you can work through the implementation at your own pace.
I will implement the library as a live-coding exercise on Fri 9-12.

# Specification

A user of the marketplace is identified by a unique username. They can take one of two roles:

- seller, listing items for sale
- buyer, biding on items

Below is the typical lifecycle of a listing in a marketplace:

1. A seller creates the listing (in draft state).
   At creation, the listing is assigned a Unique ID within a marketplace.
   The following data needs to be specified for a listing:

   - title, a string of max length 50
   - start price, a `Price` (see below)
   - description, a string of max length 500
   - min bidding time, a [`timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects)

   Some or all of this data can be specified and modified after creation.

2. The seller can change the listing state from draft to active at any time, as long as all data from point 1 above has been specified. Alternatively, the seller can change the lifting state from draft to cancelled.

3. When the listing is active, buyers can submit bids. Only the current highest bid is visible to buyers. Each buyer can have at most one bid on the listing at any time and can withdraw their bid at any time. A new bid can be submitted only if it is higher than the highest current bid.

4. After the minimum bidding time has elapsed from the moment the listing has become active, the seller can change the listing state from active to sold, as long as at least one bid is present: when this happens, the buyer with the highest bid has bought the item. At any time when no bids are present, the seller can change the listing state from active to cancelled.

A `Marketplace` class should act as the entry point to your library, such that all data and actions for a single marketplace should ultimately be accessible starting from a corresponding `Marketplace` instance.
This is an example of the **Façade Pattern**, where a library or application has a single entry point which provides access to all of its functionality, typically by exposing other classes.

The library should offer the following core functionality:

- Creation of listings, either brand new or from existing listings.
- Access to listings by ID.
- Editing of listing data, with undo functinoality. Changes to listing state.
- Submission and management of bids on the listing. A generic data structure should abstract part of the functionaltiy for bid keeping.
- For a given seller: access their draft, active, sold and cancelled listings.
- For a given buyer: access their current bids on active listings and the listings they have bought.
- Event subscription functionality, where can request to be notified of the following events:
  - changes in state for a listing
  - changes in bis for a listing
- Keeping track of: total amount of money that a seller has made from sold listings; total amount of money that a buyer spent on listings they bought; amount of money that a buyer currently has on highest bids for active listings. This can be done using the event subscription functionality.
- Query functionality on listings, based on various criteria (data, status, bidding status, etc).
- Price specification with currency conversion functionality (say GBP, EUR and USD). You can base conversion on a mock global object, with a method providing live exchange rates for a given currency pair: in reality, this would manage a connection to some online service, but you should just return some fixed numbers.

Data management and actions for distinct clusters of marketplace functionality should be delegated to distinct classes.
This is according to the **Single Responsibility Principle**: every component &mdash; module, class, method, function &mdash; should have a single well-defined responsibility (at the corresponding level of abstraction).

# Implementation

Tree of public modules and classes for this mini-project:

```
marketplace
├── __init__.py
├── listings.py
│   └── Listing
├── bids.py
│   └── BidStack
├── users.py
│   ├── User
│   ├── Buyer
│   └── Seller
├── marketplaces.py
│   └── Marketplace
├── queries.py
│   └── ListingQuery
└── utils
    ├── __init__.py
    ├── stacks.py
    │   └── WithdrawableStack
    ├── timekeeping.py
    │   └── TimeServer
    └── prices.py
        ├── Forex
        └── Price
```

Please enable [PEP 563 – Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/) by placing the following line at the top of your module imports:

```py
from __future__ import annotations
```

PEP 563 will be ultimately superseded by [PEP 649 – Deferred Evaluation Of Annotations Using Descriptors](https://peps.python.org/pep-0649/) in Python 3.14, but for now it fixes some important issues with Python's static type annotations.


## Part 1 - Listings

Implement a `Listing` class responsible for all listing-related functionality.

You will need to reference the `Seller` and `Buyer` classes from `marketplace.users` in some of your type hints: to avoid circular imports in your modules, you should import this classes solely for static type-checking purposes, as shown below.

```py
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import Buyer, Seller
```

Until you implement them, you can use mock implementations of `Seller` and `Buyer`:

```py
# in users.py
class Seller: ...
class Buyer: ...
```

### Listing reation

Implement the constructor `__new__` for listings, taking a seller and a string UID as inputs.
The responsibility for UID management will lie with the `Marketplace` class: this is an example of the Factory Pattern, where one class is resposible for creating instances of another class by supplying additional information which it manages internally.

Implement an instance method `clone` for listings, taking a seller and a string UID as inputs and returning a draft copy of the current listing with the same listing data but a new seller and UID.
This is an example of the Prototype Patter, where an existing instance of a class is used as a blueprint to create another instance, instead of invoking the constructor.

Here are three suggestions on how to implement `clone`:

- You might delegate construction responsibility within `clone` to `__new__`, then manually set the relevant data on the new draft listing.
- You might delegate construction resposibility within both `clone` and `__new__` to a protected constructor `_new`, allowing you to specify the initial data together with the seller and UID.
- You might delegate construction responsibility within `clone` to `__new__`, then manually set the relevant data using the `restore` method described below.

### Listing data

Implement properties exposing the title, price, description and minimum bidding time.
Remember that these might not be set: you might signal this by returning `None`, or by raising an error.

Implement methods which allow each one of the above pieces of data to be set and modified, but only when the listing is in the draft state.
Remember to validate input to these methods when the constraints cannot be captured by the static type hints.

In order to support undo functionality in the editing of draft listings, implement the Memento Pattern:

- a `memento` property returns a "memento", a snapshot of the current listing data;
- a `restore` method sets listing data to the values stored in the given memento.

Depending on how you implement the memento and/or the restore method, you may or may not need to perform validation of the input data.


### Listing states

Implement a property `state` which exposes the listing state, as well as methods `activate`, `cancel` and `sell` which performs legal state transitions.

Implement properties exposing all state dependent data:

- listing time (a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects)) for active and sold listings
- bids, for active listings (use a mock implementation of `BidStack`)
- selling price (a `Price`), selling time (a `datetime`) and buyer for sold listings
- cancelling time (a `datetime`) for cancelled listings

Your properties should raise errors if the listing is not in the relevant state.
Similarly, state transition methods should raise error if their preconditions are not met.
This is an example of the State Pattern, where an object changes its behaviour depending on its internal state.


## Part 2 - Bid Management

### Reusable generic data structure

Implement a generic reusable data structure for a "withdrawable stack", supporting the following operations:

- `peek`ing at the top item of the stack
- `push`ing an item on the top of the stack
- `pop`ping an item from the top of the stack
- counting the number of items in the stack (use `__len__`)
- checking if an item is in the stack (use `__contains__`)
- `remove`ing an item from the stack, if it is in the stack

Elements in the stack must be hashable and unique (compared with `==`).
Pushing raises error if the element being pushed on top of the stack is already present in the stack.
The `remove` method takes the item to be removed as its argument, not the item's position (which is not exposed to the outside).

```py
from collections.abc import Hashable
from typing import Generic
ItemT = TypeVar("ItemT", bound=Hashable)
class WithdrawableStack(Generic[ItemT]):
    ...
```

### Bids stack

Define a type alias `Bid` for bid data, as a pair of a buyer and a price.
This is an example of a low-level data container, with no logic associated, so you shouldn't use a class for this.

Implement a `BidStack` class responsible for bid management functionality on an active listing:

- `place`ing a new bid, subject to conditions and invalidating any previous bid by the same buyer
- `withdraw`ing a bid
- accessing the current `top` bid
- checking whether there are bids (use `__bool__` and/or `__len__`)

The `BidStack` class should use a `WithdrawableStack[Bid]` internally, but it should not inherit from it: a stack of bids can use a withdrawable stack to power its logic, but it is behaviourally different from one, and so it shouldn't be a subclass according to the **Liskov Substitution Principle**.
This is an example of **composition over inheritance**.

## Part 3 - Users

...

## Part 4 - The Marketplace Façade

...

## Part 5 - Event Management

...

## Part 6 - Query Functionality

...

## Part 7 - Prices and Timekeeping

...
