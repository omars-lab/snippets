package LearningScalaSnippets;

object JsonPath extends App {

  val schemaString = """{
		"schema": {
			"type": "record",
			"name": "purchase",
			"fields": [
				{"name": "id", "type": "string"},
				{"name": "purchaseId", "type": "string"},
				{ "name": "name", "type": "string"},
				{"name": "cost", "type": "string"},
				{"name": "category", "type": "string"}
			]
		},
		"schema.row.field": "id"
	}"""

  gatlingJSONPath(schemaString)
  pimpathonJSONPath(schemaString)

  object gatlingJSONPath {
    def apply(str: String): Unit = {
      val stuff = for {
        x <- \/.fromEither(str.parse)
        iter <- \/.fromEither(JsonPath.query("$.schema", x))
      } yield iter
      stuff.getOrElse(List().toIterator: Iterator[Any]).foreach(println)
    }
  }

  object pimpathonJSONPath {
    def apply(str: String): Unit = {
      import pimpathon.argonaut.JsonFrills
      // Using JSON Path - Needs a library with a custom resolver
      // Decendent thing my be broken ... what if you have a key called string? - yep it is!
      // ... the python path stuff in general is broken... or at least it assumes that all things its coded against have the same schemas.
      println(
        for {
          x <- str.parseOption
        } yield {
          val list1 = x.descendant("$.schema.fields[*].name").string.getAll
          val list2 = x.descendant("$.schema.fields[*].type").string.getAll
          list1.zip(list2)
        }
      )
    }
  }

  object argonautJSONPath {
    def apply(str2: String): Unit = {
      import argonaut.JsonPath.root
      val str = """{"string": ["1", "2"]}"""
      val stuff = for {
        j <- \/.fromEither(str.parse)
      } yield {
        println(root.selectDynamic("string").each.json.getAll(j).zip(root.selectDynamic("string").each.json.getAll(j)))
        println(root.selectDynamic("string").each.string.getAll(j).zip(root.selectDynamic("string").each.string.getAll(j)))
      }
      stuff.getOrElse(())
    }
  }
}
