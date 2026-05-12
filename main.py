from graph_flow import graph

print("=== AI Content Router ===")

user_topic = input("Enter topic: ")

result = graph.invoke({
    "topic": user_topic,
    "persona": "",
    "response": ""
})

print("\nFINAL OUTPUT\n")

print(result["response"])