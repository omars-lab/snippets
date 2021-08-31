package com.oeid.SpringHelloWorld;

class TodoNotFoundException extends RuntimeException {

    TodoNotFoundException(Long id) {
        super("Could not find employee " + id);
    }
}