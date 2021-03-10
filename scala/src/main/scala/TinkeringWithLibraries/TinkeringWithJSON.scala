package TinkeringWithLibraries

import argonaut.Argonaut._
import argonaut._

object Obj {

  case class UserProfile[R: DecodeJson](username: String, addresses: R)
  object UserProfile {
    // Sample of explicitly implementing encoder / decoder for a class ...
    implicit def UserProfileDecodeJson[R: DecodeJson]: DecodeJson[UserProfile[R]] =
      DecodeJson(
        c => for {
          username <- (c --\ "username").as[String]
          addresses <- (c --\ "addresses").as[R]
        } yield UserProfile(username, addresses)
      )
    implicit def UserProfileEncodeJson[R: EncodeJson]: EncodeJson[UserProfile[R]] =
      EncodeJson((ir: UserProfile[R]) =>
        ("username" := ir.username)
          ->: ("addresses" := ir.addresses)
          ->: jEmptyObject)
  }

  case class AddressAsCaseClass(city: String, state: String, country: String)
  object AddressAsCaseClass{
    // Sample of leveraging a built in case class codec!
    implicit def AddressJsonAsCaseClass: CodecJson[AddressAsCaseClass] =
      casecodec3(AddressAsCaseClass.apply, AddressAsCaseClass.unapply)("CITY", "STATE", "COUNTRY")
  }

  type AddressAsBuiltIn = Map[String,String]

}

object SimpleApp extends App {
  import Obj._

  val json1 =  """{"username":"hi", "addresses": [{"CITY":"Austin", "STATE": "Tx", "COUNTRY": "USA"}]}"""
  println(json1.parseOption.map(j => j.as[UserProfile[List[AddressAsCaseClass]]].result));

  val json2 =  """{"username":"hi", "addresses": [{"CITY":"Austin", "STATE": "Tx", "COUNTRY": "USA"}]}"""
  println(json2.parseOption.map(j => j.as[UserProfile[List[AddressAsBuiltIn]]].result));

}
