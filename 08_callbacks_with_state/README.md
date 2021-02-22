# App State

We can use the `state` to control when the app is updated after the user makes a change to the inputs. By default, Dash will update as soon as the change occurs, but we can change this behavior. We can think of this as hitting a submit button on a form.

To achieve this, we need to add `State()` to the `@app.callback` along with the standard `Input()` and `Output()` calls. The state needs to be connected to a component and a property to report back to.

We can thus think about the state as "everything that we want to hold, until a certain action occurs".
