AirBnB clone project
Command interpreter to manage AirBnb objects

Parent class (BaseModel) to take care of initialization, serialization, and deserialization of future instances
Flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
Creates all classes used for AirBnb (User, State, City, Place that inherit from BaseModel
Creates the first abstracted storage engine of the project: File storage
Creates all unittests to validate all our classes and storage engine
