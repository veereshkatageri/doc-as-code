.. _display_code_snippets:

Displaying code snippets
++++++++++++++++++++++++

This page is intended to show how to use code snippets in doc-as-code.

.. contents:: Table of contents
    :local:

Syntax
======

Source code listings / snippets shall be displayed in a monospaced font. 

1. The syntax to include python code snippets

.. code-block :: python

    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)

2. The syntax to include java code snippets

.. code-block:: java

    public class Main {
        public static void main(String[] args) {
            System.out.println("This will be printed");
        }
    }

3. The syntax to include cpp code snippets

.. code-block:: cpp

    /**
    * seconds from midnight
    */
    long GetTime(void){
        return secondFromMidnight(CURRENT);
    }
    /**
    # @overload void GetTime(int &hours, int &minutes, int &seconds)
    */
    void GetTime(int &hours, ///< set: current hour
                int &minutes, ///< set: current minutes
                int &seconds) { ///< set: current seconds
    hours = _hours;
    minutes = _minutes;
    seconds = _seconds;
    }

The above code snippets can be visualized as follows

#. python

   .. code-block :: python
   
       def scope_test():
           def do_local():
               spam = "local spam"
   
           def do_nonlocal():
               nonlocal spam
               spam = "nonlocal spam"
   
           def do_global():
               global spam
               spam = "global spam"
   
           spam = "test spam"
           do_local()
           print("After local assignment:", spam)
           do_nonlocal()
           print("After nonlocal assignment:", spam)
           do_global()
           print("After global assignment:", spam)
   
       scope_test()
       print("In global scope:", spam)

#. java

   .. code-block:: java
   
       public class Main {
           public static void main(String[] args) {
               System.out.println("This will be printed");
           }
       }

#. cpp

   .. code-block:: cpp
   
      /**
       * seconds from midnight
       */
      long GetTime(void){
          return secondFromMidnight(CURRENT);
      }
      /**
       # @overload void GetTime(int &hours, int &minutes, int &seconds)
       */
      void GetTime(int &hours, ///< set: current hour
                   int &minutes, ///< set: current minutes
                   int &seconds) { ///< set: current seconds
       hours = _hours;
       minutes = _minutes;
       seconds = _seconds;
      }
