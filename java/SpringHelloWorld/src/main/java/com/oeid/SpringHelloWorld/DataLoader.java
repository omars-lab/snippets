package com.oeid.SpringHelloWorld;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
class DataLoader {

	private static final Logger log = LoggerFactory.getLogger(DataLoader.class);

	@Bean
	CommandLineRunner initDatabase(TodoRepository repository) {

		return args -> {
			log.info("Preloading " + repository.save(new Todo("Bilbo Baggins", "burglar")));
			log.info("Preloading " + repository.save(new Todo("Frodo Baggins", "thief")));
		};
	}
}