from collections import defaultdict
import math
import networkx as nx
import matplotlib.pyplot as plt

class Node:
	def __init__(self, name):
			self.Name = name

class Elo:
	def __init__(self, parentNode: Node, childNode: Node, weight:float):
		self.parentNode = parentNode
		self.childNode = childNode
		self.weight = weight

class Grafo:
	def __init__(self, isDirected: bool = False) -> None:
		self.Nodes = defaultdict(Node)
		self.Elos = []
		self.Name2Int = {}
		self.isDirected = isDirected	
		
	def addNode(self, node: Node):

		if type(node.Name) is str and node.Name not in self.Name2Int: # Caso seja uma string salvar um dicionario com numeros correspondentes aos nomes, para o print geral do grafo
			self.Name2Int.update({node.Name: len(self.Nodes)})

		self.Nodes.update({node.Name: node})

	def addElo(self, currentNode: Node, nextNode: Node, weight:float):
		""" Criação de um elo entre 2 Nodes, os salvando em uma lista de Elos
				e adicionando os novos nodes no dicionario de Nodes existentes.
		"""

		if currentNode.Name in self.Nodes:
			currentNode = self.Nodes.get(currentNode.Name)
		else:
			self.addNode(currentNode)

		if nextNode.Name in self.Nodes:
			nextNode = self.Nodes.get(nextNode.Name)
		else:
			self.addNode(nextNode)
		
		if self.isDirected:
			for item in self.Elos:
				if item.parentNode == currentNode and item.childNode == nextNode:
					return
			self.Elos.append(Elo(currentNode, nextNode, weight))
		else:
			for item in self.Elos:
				if item.parentNode == currentNode and item.childNode == nextNode or item.parentNode == nextNode and item.childNode == currentNode:
					return
			self.Elos.append(Elo(currentNode, nextNode, weight))


	def getWeight(self, startPoint: str, to: str) -> float:
		currLocation = self.Nodes.get(startPoint)
		nextLocation = self.Nodes.get(to)
		
		if self.isDirected:
			for index, item in enumerate(self.Elos):
				if item.parentNode == currLocation and item.childNode == nextLocation:
					return self.Elos[index].weight
		else:
			for index, item in enumerate(self.Elos):
				if item.parentNode == currLocation and item.childNode == nextLocation:
					return self.Elos[index].weight
				elif item.parentNode == nextLocation and item.childNode == currLocation:
					return self.Elos[index].weight
		return None

