# iOS concurrency fact sheet

* NSInvocationOperation is a class you use as-is to create an operation object based on an object and selector from your application.
* When you create a block operation, you typically add at least one block at initialization time; you can add more blocks as needed later. When it comes time to execute an NSBlockOperation object, the object submits all of its blocks to the default-priority, concurrent dispatch queue. The object then waits until all of the blocks finish executing.
* `start`, `isExecuting`, `isFinished`, and `isConcurrent` are required to override for concurrent operations.
* A canceled operation is still considered to be "finished".
* The system provides each application with four concurrent dispatch queues. These queues are global to the application and are differentiated only by their priority level.
* Use the dispatch_get_current_queue function for debugging purposes or to test the identity of the current queue.
* All dispatch objects (including dispatch queues) allow you to associate custom context data with the object. To set and get this data on a given object, you use the dispatch_set_context and dispatch_get_context functions.
* Executing a completion callback after a task

```objective-c
void average_async(int *data, size_t len,
   dispatch_queue_t queue, void (^block)(int))
{
   // Retain the queue provided by the user to make
   // sure it does not disappear before the completion
   // block can be called.
   dispatch_retain(queue);

   // Do the work on the default concurrent queue and then
   // call the user-provided block with the results.
   dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
      int avg = average(data, len);
      dispatch_async(queue, ^{ block(avg);});

      // Release the user-provided queue when done
      dispatch_release(queue);
   });
}
```

* Using Dispatch Semaphores to Regulate the Use of Finite Resources

```objective-c
// Create the semaphore, specifying the initial pool size
dispatch_semaphore_t fd_sema = dispatch_semaphore_create(getdtablesize() / 2);

// Wait for a free file descriptor
dispatch_semaphore_wait(fd_sema, DISPATCH_TIME_FOREVER);
fd = open("/etc/services", O_RDONLY);

// Release the file descriptor when done
close(fd);
dispatch_semaphore_signal(fd_sema);
```

* Dispatch groups are a way to block a thread until one or more tasks finish executing.
* Do not call the dispatch_sync function from a task that is executing on the same queue that you pass to your function call. Doing so will deadlock the queue. If you need to dispatch to the current queue, do so asynchronously using the dispatch_async function.


All contents are from [Apple concurrency programming guide](https://developer.apple.com/library/content/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091-CH1-SW1)
