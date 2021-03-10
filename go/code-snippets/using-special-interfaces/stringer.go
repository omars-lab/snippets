// https://tour.golang.org/methods/18

package main

import "fmt"

type IPAddrAlternativeByValue [4]byte

func (ip IPAddrAlternativeByValue) String() string {
	return fmt.Sprintf("%v.%v.%v.%v", ip[0], ip[1], ip[2], ip[3])
}


type IPAddrAlternativeByReference [4]byte

func (ip * IPAddrAlternativeByReference) String() string {
	return fmt.Sprintf("%v.%v.%v.%v", (*ip)[0], (*ip)[1], (*ip)[2], (*ip)[3])
}


func main() {

	hosts_1 := map[string]IPAddrAlternativeByValue{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}
	for name_1, ip_2 := range hosts_1 {
	  fmt.Printf("%v: %v\n", name_1, ip_2)
	}

	hosts_2 := map[string]IPAddrAlternativeByReference{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}
	for name_2, ip_2 := range hosts_2 {
	  fmt.Printf("%v: %v\n", name_2, &ip_2)
	}

}
