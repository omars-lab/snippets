# Adding Methods to Types

## Attaching Methods to Types
How can I define a method on a class?
	https://tour.golang.org/methods/1

What can I define methods on?
	> You can only declare a method with a receiver whose type is defined in the same package as the method. You cannot declare a method with a receiver whose type is defined in another package (which includes the built-in types such as int).
	> https://tour.golang.org/methods/3


## Accessing Instances in Type Methods
- How do I access an instance from it's method? or a pointer to the instance?
	- https://tour.golang.org/methods/6
	- https://tour.golang.org/methods/7
	- https://tour.golang.org/methods/8

@import "../code-snippets/adding-methods/adding-methods.go"


## Overriding Methods
- Can method be overwritten?
	- Without subclassing ... no ...
		- https://medium.com/random-go-tips/method-overriding-680cfd51ce40

## Deciding on Method Attachment Alternatives
Should I attach a method to the pointer of the class or the class itself?
		- Attach method to pointer if ...
			- If I want to change the internals of a class ... then a pointer ...
			- Don't want to copy whole ds every time I call method ...
			- https://tour.golang.org/methods/8
			- https://tour.golang.org/methods/4
		- Don't mix and match ...
		- Be cautious of interfaces ... if a method is attached to a pointer ... then the pointer to the class implements the interface ... and not the  class itself ... https://tour.golang.org/methods/9
