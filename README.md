# Linear Probing Hash 🔑🗄️
Linear probing hash is a software to visualize the creation and manipulation of a hash table with linear-probing collision treatment for a better understanding.

## Linear Probing Collision Treatment 🔍🎯

Collision handling in a hash table using linear probing is a technique used to deal with situations where two or more calculated hash keys result in the same table index, i.e. a collision occurs.

A hash table is a data structure that allows the storage and fast retrieval of elements associated with unique keys. It uses a hash function to convert the keys into table indexes where the elements are stored. However, when two different keys produce the same index, a collision occurs.

Linear probing is one of the common approaches to resolve collisions in a hash table. In this technique, when a collision occurs, the element with the duplicate hash key is simply placed in the next available position in the table. The idea is to do a sequential search through subsequent indexes until an empty position is found where the element can be stored.

For example, suppose the hash function produced the same index for two different keys:

 1. Key A -> Hash (index) = 5
 2. Key B -> Hash (index) = 5 (collision)

If there is a collision, the hash table is updated as follows using linear probing:

 1. Index 5: Key A (first key calculated).
 2. Index 6: Key B (second calculated key, placed at the next available index after 5)

It is worth noting that when searching for an available position, it is necessary to take into account that the hash table can be circular, i.e. the search can continue from the beginning of the table if it has reached the end.

## Tecnologies 🔧
- [Python](https://www.python.org)
- [PyQt6](https://pypi.org/project/PyQt6/)

## Usage 💻
To use the program, simply install and run the `LinearProbingHash1.0.exe` file generated in the latest [release](https://github.com/fsoupimenta/linear-probing-hash/releases/tag/1.0).

When the program starts, it will open the screen below in which the user must enter the size of the hash table, this size being a prime number greater than 2. If the user does not enter anything, the software will use the size 23 by default:

![Screenshot_150](https://github.com/fsoupimenta/linear-probing-hash/assets/108306295/6f7d63d6-41bd-4912-8c94-28b2de6ffde1)

After that, the main screen below will appear showing the table and the operations that can be performed.

![Screenshot_151](https://github.com/fsoupimenta/linear-probing-hash/assets/108306295/28e3719c-ae23-4e27-afea-8c2c33869ca8)

## Features 🚀
<table>
<tbody>
  <tr>
    <th> Name </th>
    <th> Functionallity </th>
  </tr>
  <tr>
    <td> Insert </td>
    <td> Inserts one key and element given by the user on input </td>
  </tr>
  <tr>
    <td> Search </td>
    <td> Searches for an element according to the key given by the user </td>
  </tr>
  <tr>
    <td> Delete </td>
    <td> Deletes an element instantly according to the key given by the user </td>
  </tr>
  <tr>
    <td> Set element available </td>
    <td> Turns an element according to the key given by the user into available to be deleted later </td>
  </tr>
  <tr>
    <td> Delete elements available </td>
    <td> Deletes all elements set as available </td>
  </tr>
</tbody>
</table>

Note that deletion from a hash table using linear probing can be done in two different ways, namely `immediate deletion` and deletion with slot marking as `available`.

- In `immediate deletion`, when an element is removed, the corresponding slot is emptied immediately, making it available for reuse. However, this approach can result in primary clustering and table fragmentation, impacting performance.
- On the other hand, deletion with slot marking as `available` avoids immediate physical removal of the element. When an element is deleted, the slot is marked as `available`, indicating that it is free to be reused. This approach avoids primary clustering, but can take up table space with slots marked as `available`.

The choice of approach depends on the specific needs of the system, considering factors such as performance, fragmentation and table space occupation.
