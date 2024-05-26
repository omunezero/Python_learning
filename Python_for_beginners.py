{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6b5cffae-bf08-41bb-92ed-ee989b23c30a",
   "metadata": {},
   "source": [
    "Python for biologists Chapter 1 and 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "15b1e317-ad11-4436-88ec-520dc98861e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "979dde5e-43a1-4403-abd1-28f5c0332e60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print('Hello world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "804e733c-40b7-4b1c-935c-b13a24ee0fad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Comments are very useful!\n"
     ]
    }
   ],
   "source": [
    "#this is a comment, it will be ignored by the computer \n",
    "print(\"Comments are very useful!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5ace85ab-a720-4938-8a46-9bbe6d407064",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "#Code for printint a text \n",
    "\n",
    "print(\"Hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3d70a13b-a6ad-4e2d-aac8-112d9a76ab27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "#Print a friendly greeting\n",
    "\n",
    "print('Hello World')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2314e2a8-df5f-4249-94b5-5c47db66e73d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (3814945402.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[4], line 3\u001b[0;36m\u001b[0m\n\u001b[0;31m    print(Hello world)\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
   "source": [
    "#Forgetting quotes\n",
    "\n",
    "print(Hello world)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "be723cc4-e503-4ad5-80d9-802d12e29309",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 1) (2036490288.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[1], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    print(\"Hello\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unterminated string literal (detected at line 1)\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\n",
    "      world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "25f0beb0-0a65-4d26-b26c-4a4373b6d202",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes\n"
     ]
    }
   ],
   "source": [
    "print('Yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c333e851-af6c-4ef9-85c9-1588ea79a996",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function print(*args, sep=' ', end='\\n', file=None, flush=False)>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a39fb568-2390-4687-855b-265cf6dc0e1f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 1) (1411358943.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[3], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    print('Hello\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unterminated string literal (detected at line 1)\n"
     ]
    }
   ],
   "source": [
    "print('Hello\n",
    "      world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cec33fe6-69c1-4d6d-a24a-84b6935cb449",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "world\n"
     ]
    }
   ],
   "source": [
    "#How to include a new line in the middle of a string\n",
    "\n",
    "print('Hello\\nworld')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4bc10516-d418-44cf-ae8e-06784e6c5280",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ATGCGTA\n"
     ]
    }
   ],
   "source": [
    "#store a short DNA sequence in the variable my_dna\n",
    "\n",
    "my_dna='ATGCGTA'\n",
    "\n",
    "#now print the DNA sequence\n",
    "\n",
    "print(my_dna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4dd4898c-77b2-4614-a981-08d11761e047",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ATGCGTA\n"
     ]
    }
   ],
   "source": [
    "my_dna='ATGCGTA'\n",
    "print(my_dna)\n",
    "#change the value of my dna\n",
    "my_dna='TGGTCCA'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0534db5b-d7fc-496f-b261-c1dcf34ba3ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_file='my_file.txt'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "80fdbe80-8fe8-4c57-9a69-84e619f59766",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my_file.txt\n"
     ]
    }
   ],
   "source": [
    "print(my_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "483785c1-d5af-4d21-b2db-0f72b88f9226",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AATTGGCC\n"
     ]
    }
   ],
   "source": [
    "#concatenation\n",
    "\n",
    "my_dna=\"AATT\" + \"GGCC\"\n",
    "print(my_dna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4018d6ba-554b-4667-8746-3d04f7aa59bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AAAATGC\n"
     ]
    }
   ],
   "source": [
    "#joining multiple strings together in one go\n",
    "\n",
    "upstream='AAA'\n",
    "my_dna=upstream+'ATGC'\n",
    "print(my_dna)\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a3b9cc25-ada7-463a-b09e-be78bc4108f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AAAATGCGGG\n"
     ]
    }
   ],
   "source": [
    "upstream='AAA'\n",
    "downstream=\"GGG\"\n",
    "my_dna=upstream+'ATGC'+downstream\n",
    "print(my_dna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5d5b6f6d-fd14-415f-babf-a23765ff6f75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Helloworld\n"
     ]
    }
   ],
   "source": [
    "print('Hello' + '' + \"world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "67c471c8-6139-4f6a-9bd4-175aec121d61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "#finding length of a string\n",
    "\n",
    "data_length=len(\"ATGC\")\n",
    "print(data_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "99606e2c-2262-4f0c-b1e7-e13d0486bd79",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[31], line 8\u001b[0m\n\u001b[1;32m      6\u001b[0m dna_length\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mlen\u001b[39m(my_dna)\n\u001b[1;32m      7\u001b[0m \u001b[38;5;66;03m#print a message telling us the DNA sequence lenght\u001b[39;00m\n\u001b[0;32m----> 8\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe length of the DNA sequence is\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m+\u001b[39m dna_length)\n",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "#example of how python treats strings and numbers differently\n",
    "\n",
    "#store the DNA sequence in a variable\n",
    "my_dna=\"ATGCGAGT\"\n",
    "#Calculate the length of the sequence and store it in a variable \n",
    "dna_length=len(my_dna)\n",
    "#print a message telling us the DNA sequence lenght\n",
    "print(\"The length of the DNA sequence is\" + dna_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "1c76ee19-b9e0-4a27-9f68-a5ea347164a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The length of the DNA sequence is8\n"
     ]
    }
   ],
   "source": [
    "#to solve this error, we use str function \n",
    "\n",
    "#store the DNA sequence in a variable\n",
    "my_dna=\"ATGCGAGT\"\n",
    "#Calculate the length of the sequence and store it in a variable \n",
    "dna_length=len(my_dna)\n",
    "#print a message telling us the DNA sequence lenght\n",
    "print(\"The length of the DNA sequence is\"  +   str(dna_length))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0cb6a14a-4877-4bfd-a644-3b58ae3ac622",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The length of the DNA sequence is 8\n"
     ]
    }
   ],
   "source": [
    "#joining two arguments without concatenation\n",
    "\n",
    "#store the DNA sequence in a variable\n",
    "my_dna=\"ATGCGAGT\"\n",
    "#Calculate the length of the sequence and store it in a variable \n",
    "dna_length=len(my_dna)\n",
    "#print a message telling us the DNA sequence lenght\n",
    "print(\"The length of the DNA sequence is\", dna_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "be5251cd-441c-4dd9-99e8-b0a127f8370c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "84b7cfcc-c78b-493e-b886-f3243204cdb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "world\n"
     ]
    }
   ],
   "source": [
    "print('Hello\\nworld')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4cd6284c-8639-44a0-bc41-f2b9bb59c4fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ATCGGTTTAAT\n"
     ]
    }
   ],
   "source": [
    "dna_seq='ATCGGTTT'\n",
    "UMI='AAT'\n",
    "\n",
    "DNA_with_UMI=dna_seq+UMI\n",
    "print(DNA_with_UMI)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4719f408-49af-4de3-8532-492e2054bc58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "lengths_of_DNA=len(DNA_with_UMI)\n",
    "print(lengths_of_DNA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2a9ebe92-5cff-42fd-b11e-15e0651d1c3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "UMI_length=len(UMI)\n",
    "print(UMI_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bf6648f3-78dd-4c91-acdd-dd7eb0085e53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The length of UMI is = 3\n"
     ]
    }
   ],
   "source": [
    "print('The length of UMI is = ' +str(UMI_length))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ce9b5a37-386f-4ebf-979a-016426d3e2e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "atgc\n"
     ]
    }
   ],
   "source": [
    "my_dna=\"ATGC\"\n",
    "#print my_dna in lower case\n",
    "print(my_dna.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6fa3aca4-bcd4-425d-acb7-10c11d373d68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "before: ATGC\n"
     ]
    }
   ],
   "source": [
    "my_dna=\"ATGC\"\n",
    "#print the variable\n",
    "print(\"before: \" + my_dna)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7f30fa5a-ffac-4300-b392-f5e5c6798da2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "after: atgc\n"
     ]
    }
   ],
   "source": [
    "#run the lower method and store the result\n",
    "lowercase_dna= my_dna.lower()\n",
    "print(\"after: \" + lowercase_dna)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53bb8b03-6c66-4aa1-8fff-3e5731d52c42",
   "metadata": {},
   "outputs": [],
   "source": [
    "#print the variable again\n",
    "print(\"after: \" + my_dna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bacab2cb-e7a7-48f6-8844-522e82319caa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ylspadktny\n",
      "ymtpadktnv\n",
      "vlspadktnv\n"
     ]
    }
   ],
   "source": [
    "#replace method\n",
    "\n",
    "protein=\"vlspadktnv\"\n",
    "#replace valine with tyrosine\n",
    "print(protein.replace('v','y'))\n",
    "#we can replace more than one character\n",
    "print(protein.replace('vls','ymt'))\n",
    "#the original variable is not affected\n",
    "print(protein)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2f430c1e-b0c6-47cc-ac4a-1373b53e200c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "vlspad\n",
      "vlspadktnv\n"
     ]
    }
   ],
   "source": [
    "#getting a substring from a long string\n",
    "\n",
    "protein=\"vlspadktnv\"\n",
    "#print positions 3 to 5 \n",
    "pa=protein[3:5]\n",
    "#postions start at 0, not 1\n",
    "print(protein[0:6])\n",
    "#id we use a stop positon beyong the end, it's the same as using the end\n",
    "print(protein[0:40])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2f9157d8-0150-435d-bab2-ce76f98f0b8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pa\n"
     ]
    }
   ],
   "source": [
    "print(pa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d48e9549-658e-4922-87e4-4ec704149a99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "vls\n",
      "ls\n"
     ]
    }
   ],
   "source": [
    "vls=print(protein[0:3])\n",
    "ls=print(protein[1:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7a2cc403-8bac-425a-845a-21f8c468234f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "v\n"
     ]
    }
   ],
   "source": [
    "protein=\"vlspadktnv\"\n",
    "first_residue=protein[0]\n",
    "print(first_residue)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "bda4dd42-0e42-4024-9796-8d1396062d13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "vlsp\n"
     ]
    }
   ],
   "source": [
    "first_4_chr=protein[0:4]\n",
    "print(first_4_chr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8e89b066-9d61-4aec-a2f8-8f37e03c5e29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valine: 2 lsp: 1 tryptophan: :0\n",
      "Valine: 2 \n",
      "lsp: 1 \n",
      "tryptophan: 0\n"
     ]
    }
   ],
   "source": [
    "#counting and finding a substring\n",
    "protein=\"vlspadktnv\"\n",
    "#count amino acids residues\n",
    "valine_count=protein.count(\"v\")\n",
    "lsp_count=protein.count(\"lsp\")\n",
    "tryptophan_count=protein.count(\"w\")\n",
    "\n",
    "all_AA_together=print(\"Valine: \" +str(valine_count), \"lsp: \"+str(lsp_count), \"tryptophan: :\" +str(tryptophan_count))\n",
    "\n",
    "all_AA_together=print(\"Valine: \" +str(valine_count), \"\\n\" \"lsp: \"+str(lsp_count), \"\\n\" \"tryptophan: \" +str(tryptophan_count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "6506cad6-ef26-42ba-9d44-0cdb65aa0f35",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valine: 2 \n",
      "Tryptophan: 0\n"
     ]
    }
   ],
   "source": [
    "print(\"Valine: \" + str(valine_count), \"\\n\" \"Tryptophan: \" + str(tryptophan_count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "e5c829f4-2781-4587-a8a8-23f86b86880e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "#Finding the location of the substring in the string\n",
    "protein=\"vlspadktnv\"\n",
    "#valine location in the string\n",
    "leucine_postion= (protein.find(\"l\"))\n",
    "print(str(leucine_postion))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "79c3c4dd-53e8-44b7-9aa9-72519c0b2a75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "#real example from DNA sequence\n",
    "\n",
    "sequence= \"AATAAAGGGCTATAAACTTACCCGCCATACCACAGATGTTCCAGATAAATATTGGAAGCTATATACGTACTTTGTTTCAAAATGGGTCAATCGAGAATATCGTCAACTGTTTACTAAAAATCAGTTTCATCAAGCAATGAAACACGCCAAAGTAAACAATTTAAGTACCGTTACTTATGAGCAAGTATTGTCTATTTTTAATAGTTATCTATTATTTAACGGGAGGAAATAATTCTATGAGTCGCTTTTGTAAATTTGGAAAGT\"\n",
    "#find a position of AATAAAGGGCTAT sequence\n",
    "print(str(sequence.find(\"AATAAAGGGCTAT\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "2c96987e-04d2-47c3-a449-4e7f38d955ea",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(str(sequence.count(\"AATAAAGGGCTAT\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "fa74dec9-58dd-471e-9858-0ec048250025",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Location: 0 \n",
      "counts: 2\n"
     ]
    }
   ],
   "source": [
    "print(\"Location: \" + str(sequence.find(\"AATAA\")), \"\\n\" \"counts: \" + str(sequence.count(\"AATAA\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "eb0ac434-656a-4e90-a8ec-7edad73f1ade",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total content of AT is : 67.9245283018868\n"
     ]
    }
   ],
   "source": [
    "#Exercises for Chapter 2\n",
    "\n",
    "DNA_sequence=\"ACTGATCGATTACGTATAGTATTGCTATCATACATATATATCGATGCGTTCAT\"\n",
    "\n",
    "total_seq=len(DNA_sequence)\n",
    "total_A_nt=DNA_sequence.count(\"A\")\n",
    "total_T_nt=DNA_sequence.count(\"T\")\n",
    "\n",
    "AT_content=((total_A_nt+total_T_nt)/total_seq)*100\n",
    "print(\"Total content of AT is : \" + str(AT_content))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c044bbab-4cd4-418f-83e1-d5a567a58f2b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TCTGTTCGTTTTCGTTTTGTTTTTGCTTTCTTTCTTTTTTTTCGTTGCGTTCTT\n",
      "ACAGAACGAAAACGAAAAGAAAAAGCAAACAAACAAAAAAAACGAAGCGAACAA\n",
      "AGTGATGGATTAGGTATAGTATTTGGTATGATAGATATATATGGATGGGTTGAT\n",
      "ACTCATCCATTACCTATACTATTTCCTATCATACATATATATCCATCCCTTCAT\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "replace expected at most 3 arguments, got 8",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[38], line 13\u001b[0m\n\u001b[1;32m     10\u001b[0m replace_G\u001b[38;5;241m=\u001b[39mDNA_seq\u001b[38;5;241m.\u001b[39mreplace(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mG\u001b[39m\u001b[38;5;124m\"\u001b[39m , \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     11\u001b[0m \u001b[38;5;28mprint\u001b[39m(replace_G)\n\u001b[0;32m---> 13\u001b[0m DNA_seq\u001b[38;5;241m.\u001b[39mreplace(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA\u001b[39m\u001b[38;5;124m\"\u001b[39m , \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mT\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mT\u001b[39m\u001b[38;5;124m\"\u001b[39m , \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mA\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC\u001b[39m\u001b[38;5;124m\"\u001b[39m , \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mG\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mG\u001b[39m\u001b[38;5;124m\"\u001b[39m , \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mTypeError\u001b[0m: replace expected at most 3 arguments, got 8"
     ]
    }
   ],
   "source": [
    "#COMPLEMENTING DNA\n",
    "\n",
    "DNA_seq=\"ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT\"\n",
    "replace_A=DNA_seq.replace(\"A\" , \"T\")\n",
    "print(replace_A)\n",
    "replace_T=DNA_seq.replace(\"T\" , \"A\")\n",
    "print(replace_T)\n",
    "replace_C=DNA_seq.replace(\"C\" , \"G\")\n",
    "print(replace_C)\n",
    "replace_G=DNA_seq.replace(\"G\" , \"C\")\n",
    "print(replace_G)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5693e6b9-a546-4129-9a95-1a312718e957",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT\n"
     ]
    }
   ],
   "source": [
    "print(DNA_seq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "abf0597e-079e-411d-893f-4def7bc01477",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f5820ae6-1dfe-4e0a-b589-d743f13a3149",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done\n"
     ]
    }
   ],
   "source": [
    "print('Done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "38800ddc-9620-4a89-b477-767921847235",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "33\n"
     ]
    }
   ],
   "source": [
    "#Restriction fragment lengths\n",
    "DNA=\"ACTGATCGATTACGTATAGTAGbAATTCTATCATACATATATATCGATGCGTTCAT\"\n",
    "\n",
    "dna_count=DNA.count('GAATTC')\n",
    "print(dna_count)\n",
    "dna_length1=DNA.find('GAATTC') + 1\n",
    "print(dna_length1)\n",
    "total=len(DNA)\n",
    "dna_length2=total-dna_length1\n",
    "print(dna_length2)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "ed74d1ae-c887-438e-87a0-d1cbe6466bb4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n",
      "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGA\n",
      "ATCATCGATCGATATCGATGCATCGACTACTAT\n",
      "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGAATCATCGATCGATATCGATGCATCGACTACTAT\n",
      "96\n"
     ]
    }
   ],
   "source": [
    "#Splicing out introns, part one\n",
    "\n",
    "sequence=\"ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT\"\n",
    "length=len(sequence)\n",
    "print(length)\n",
    "exon1=sequence[0:63]\n",
    "print(exon1)\n",
    "exon2=sequence[90:123]\n",
    "print(exon2)\n",
    "\n",
    "coding_region= exon1+exon2\n",
    "print(coding_region)\n",
    "print(len(coding_region))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "6ebc6073-4714-42ae-942e-8f8d1ff73cec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Percentage of the coding DNA sequence is: 78.04878048780488\n"
     ]
    }
   ],
   "source": [
    "#Splicing our introns, part two\n",
    "sequence=\"ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT\"\n",
    "length=len(sequence)\n",
    "exon1=sequence[0:63]\n",
    "\n",
    "exon2=sequence[90:123]\n",
    "\n",
    "coding_region= len(exon1+exon2)\n",
    "percentage = (coding_region/length*100)\n",
    "print(\"Percentage of the coding DNA sequence is: \" + str(percentage))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "06143edd-e541-4fa3-bc63-5e52bfcf9cd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n",
      "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGAtcgatcgatcgatcgatcgatcatgctATCATCGATCGATATCGATGCATCGACTACTAT\n"
     ]
    }
   ],
   "source": [
    "#Splicing our introns, part three\n",
    "\n",
    "sequence=\"ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT\"\n",
    "print(len(sequence))\n",
    "exon1=sequence[0:63]\n",
    "\n",
    "introns=sequence[63:90]\n",
    "\n",
    "exon2=sequence[90:123]\n",
    "\n",
    "\n",
    "print(exon1+introns.lower()+exon2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "2b95d82f-34b1-4a3d-b2ca-4ffe5a075ed8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n"
     ]
    }
   ],
   "source": [
    "my_dna=\"ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGAtcgatcgatcgatcgatcgatcatgctATCATCGATCGATATCGATGCATCGACTACTAT\"\n",
    "print(len(my_dna))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "947d8adc-7fc3-4ad2-975a-83e74c59019f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chapter 2 of python for biologists is done\n"
     ]
    }
   ],
   "source": [
    "print('chapter 2 of python for biologists is done')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
