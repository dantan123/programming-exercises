import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var, values in self.domains.items():
            for val in values.copy():
                if var.length != len(val):
                    self.domains[var].remove(val)
        return
        raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        found = False
        #print("x domain is", self.domains[x])
        #print("y domain is", self.domains[y])
        i,j = self.crossword.overlaps[x,y]
        #print("the overlap square is",i,j)

        for xval in self.domains[x].copy():
            for yval in self.domains[y]:
                if xval[i] == yval[j]:
                    #print("found")
                    found = True
                    break
                else:
                    continue
            
            # keep track of whether a value is found for each xval iteration
            if found == False:
                #print("about to remove")
                self.domains[x].remove(xval)
            else:
                found = False
        return revised
        raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # create an empty queue list
        queue = []
        if arcs == None:
            for i in self.crossword.variables:
                for j in self.crossword.neighbors(i):
                    queue.append((i,j))
        else:
            queue = arcs
        
        #print(queue)
        
        # while not empty
        while queue:
            var = queue.pop(0) #FIFO
            x = var[0]
            y = var[1]
            if self.revise(x, y): # call revise
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x):
                    if z == y:
                        continue
                    else: 
                        queue.append((z,x))
        print("the queue is now", queue)
        return True
        raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # check that all variables are in the assignment
        for var in self.domains:
            if var not in assignment:
                return False

        # check that each variable has a corresponding value
        for val in assignment.values():
            if not val:
                return False
        return True
        raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        all_vals = []
        for var, val in assignment.items():
            # check value is the correct length
            if var.length != len(val):
                return False
            
            # check val is unique
            if val in all_vals:
                return False
            all_vals.append(val)

            # check no conflicts with neighbors
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    i, j = self.crossword.overlaps[var, neighbor]
                    if assignment[var][i] != assignment[neighbor][j]:
                        return False
        return True
        raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        vals = self.domains[var]
        print("the list of values is", vals)
        return vals

        """
        ordered_vals = []
        val_list = []

        for val in self.domains[var]:
            count = 0
            # val in assignment is not counted
            if val in assignment.values():
                continue
            for neighbor in neighbors:
                if self.crossword.overlaps[var, neighbor]:
                    # if there is overlap with neighbor, then check
                    assignment[neighbor] = val
                    if self.consistent(assignment) == False:
                        count += 1
                    assignment[neighbor].remove(val)
            ordered_vals.append((val, count))
        
        ordered_vals.sort(key = count)
        """
        raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # use min # of remaining values
        for var, values in self.domains.items():
            if var not in assignment:
                return var
        raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            print("the assignment is", assignment)
            return assignment
        var = self.select_unassigned_variable(assignment)
        print("the selected variable is", var)
        for value in self.order_domain_values(var, assignment):
            if self.consistent(assignment): # check if the assignment is consistent
                assignment[var] = value
                print("the new assignment is", assignment[var])
                result = self.backtrack(assignment)
                if result != None:
                    return result
                else:
                    assignment.pop(var)
        return None
        raise NotImplementedError

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)

if __name__ == "__main__":
    main()
