# import section *********
import oops
import datastructure as dt
import recursion as rec


"""""
department =[("Game Design","Nishant Sinha",10),
             ("Game Development", "Pushkar",10),\
             ("Account", "shubham Sindhu",10),
             ("Marketing", "Rajeev Kumar", 10),
             ("Resouces","Nikita Barua",10),
            ]
projects_data = [
     ("Robo Runner","Marketing", 9 , 8,"10/12/2020"),
     ("Adventure","Game Design",9,8,"12/11/2020"),
     ("Buzzoni","Game Development",9,8,"12/11/2020")
]

employee = [
     ("A",25,"F","Game Design",30000),
     ("B",25,"F","Game Design",30000),
     ("C", 25, "F", "Game Design", 30000)
]"""


if __name__ == '__main__':
     """
     print("***************************************** Organization Management ****************************")
     print(" ")
     org = oops.Organization("Vasi Game", "Rajesh" , 2017, "Gaming")
     org.show_organization()
     print(" ")
     departments = []
     projects = []
     employees = []
     for item in department:
          departments.append(oops.Department(item))

     for item in projects_data:
          projects.append(oops.Project(item))

     for item in employee:
          employees.append(oops.Employee(item))
     print("************************************ Departments  ****************************")
     print(" ")
     for i in departments:
          i.show_department()
     print(" ")
     print("**********************************  Projects ****************************")
     print(" ")
     for i in projects:
          i.show_project()
     print(" ")
     print("**********************************  Employee ****************************")
     print(" ")
     for i in employees:
          i.show_employee()


     print("************************** Stack Operation ************************")
     stack = dt.Stack()
     stack.push(1)
     stack.push(2)
     stack.show_stack()
     print(stack.peek())
     stack.pop()
     stack.show_stack()

     print("**************************** Queue Operation *************************")
     queue = dt.Queue()
     queue.push(1)
     queue.push(2)
     queue.push(3)
     queue.show_queue()
     queue.pop()
     queue.show_queue()
     print(queue.peek())


     print("********************************* Max Heap oprations ***************************")
     max_heap = dt.MaxHeap([])
     max_heap.show_max_heap()
     max_heap.push(13)
     max_heap.push(18)
     max_heap.show_max_heap()
     print(max_heap.getMax())
     max_heap.pop()
     max_heap.show_max_heap() """



     """
     print("******************************* Single Linked List Operation **************************")
     ll = dt.Single_linked_list()
     ll.show_linkedlist()
     ll.add(2)
     ll.add(14)
     ll.add(12)
     ll.add(1)
     print(f"Size : {ll.size}")
     ll.show_linkedlist()
     print(ll.find(13))
     print(ll.remove(1))
     ll.show_linkedlist()   """


     """
     print("************************* Circular Linked List Operation ****************************************")
     cll = dt.Circular_linkedList()
     print(cll.size)
     for i in range(1,12):
         cll.add(i)
     print(cll.find(2))
     print(cll.remove(2))
     cll.show_linked_list() """""

     """"
     print("***************************** Double linked List ***********************************")

     dll = dt.Double_linkedList()
     for i in range(1,12):
         dll.add(i)

     print(dll.add(12))
     print(dll.find(13))
     print(dll.find(11))
     print(dll.remove(14))
     print((dll).remove(12))
     dll.show_linked_list() """""""""""


     """"" print("********************** BST ****************************************")

     bst = dt.BinaryTree(7)
      bst.insertNode(9)
     for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
         bst.insertNode(i)
     bst.preorder()
     print("Preorder Traversal")
     bst.inorder()
     print()
     bst.postorder()
     print("Postorder Traversal")
     print(f"number of elements {bst.get_size()}")
     print(f"16 is there {bst.findNode(16)}")
     print(f"15 is there {bst.findNode(15)}")"""""""""""

     # string permutation //////////////////////////////
     rec.string_permutation("ABC")

     """"
     print("************************* Boggle problem **********************")
     board = [
         ['G','I','Z'],
         ['U','E','K'],
         ['Q','S','E']
     ]
     visited =[
         [False,False,False],
         [False, False, False],
         [False, False, False],
     ]
     dictionary = ['GEEKS','GEEK','FOR','GO','QUIZ']
     word = ""
     for i in range(0,len(board)):
         for j in range(0,len(board)):
             visited[i][j] = True
             rec.findWord(board,visited,0,0,word+board[i][j],dictionary)
             visited[i][j] = False """""""""""
     """"
     print("*************** Rat in Maze ***************************")
     maze = [
         [1,1,0,1],
         [0,1,1,1],
         [0,1,0,1],
         [0,1,1,1]
     ]
     visited = [
         [0,0,0,0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]
     ]
     visited[0][0] = 1
     print("This the Maze ")
     for i in range(0,len(maze)):
         print(maze[i])
     rec.findMazePath(maze,visited,0,0,3,3,1)"""""

     """""
     print("***************** Knight Tour ****************************")
     visited = [
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]
     ]
     visited[0][0] = 1
     rec.knightTour(visited,0,0,1) """
     """"
     print("******************* N Queen Problem *****************************")
     board = [
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False]
     ]
     rec.nQueen(board,-1,8)"""""

     """""
     print("******************* Grid Unique Path *********************")
     print(rec.uniqeGridPath(3,4))

     print("***************** Number of partition of given list in upto range **********************")
     print(rec.count_partition(9,5))"""""""""







