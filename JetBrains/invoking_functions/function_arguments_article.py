def main():
    article = """
    ## Where Do We Specify the Arguments of a Function? 

    This lesson is brought to you by JetBrains.

    ### Introduction

    In Python programming, understanding where to specify the arguments of a function is crucial for writing clear and effective code. The answer is simple: **in parentheses**. Let's explore this concept with examples and demonstrations to make it easy to grasp.

    ### What Are Function Arguments?

    Function arguments are the values you pass to a function when you call it. These values are used by the function to perform its task. Specifying arguments correctly ensures that your function has the data it needs to operate.

    ### Specifying Arguments in Parentheses

    When you define a function, you use parentheses to specify any parameters it can accept. Similarly, when you call a function, you use parentheses to pass the arguments. Let's look at some examples to illustrate this.

    ### Example 1: A Simple Greeting Function

    ```python
    def greet(name):
        print(f"Hello, {name}!")

    greet("Dante")
    ```

    In this example, the function `greet` takes one argument, `name`. When we call the function with `greet("Dante")`, the argument `"Dante"` is passed inside the parentheses. The function then prints "Hello, Dante!".

    ### Example 2: Adding Two Numbers

    ```python
    def add(a, b):
        return a + b

    result = add(3, 5)
    print(result)  # Output: 8
    ```

    Here, the `add` function takes two arguments, `a` and `b`. When we call `add(3, 5)`, the arguments `3` and `5` are specified inside the parentheses. The function returns their sum, which is `8`.

    ### Why Parentheses?

    Using parentheses to specify arguments is a clear and consistent way to indicate the inputs a function needs. It helps keep the code readable and organized. Imagine if we used different symbols like curly braces `{}` or square brackets `[]`—it would make the code harder to read and understand.

    ### Common Mistakes

    A common mistake is to forget the parentheses when calling a function, especially if the function doesn't take any arguments. For example:

    ```python
    def say_hello():
        print("Hello!")

    say_hello  # This won't call the function
    say_hello()  # This will call the function
    ```

    In the first case, `say_hello` without parentheses refers to the function itself, not its execution. Adding the parentheses `say_hello()` correctly calls the function.

    ### Conclusion

    Specifying arguments in parentheses is a fundamental aspect of Python programming. It ensures that functions receive the necessary inputs to perform their tasks. By mastering this simple concept, you can write more effective and readable code.

    This article was inspired by a lesson from JetBrains. For more in-depth tutorials and lessons, be sure to check out their resources.
    """
    print(article)

if __name__ == "__main__":
    main()
