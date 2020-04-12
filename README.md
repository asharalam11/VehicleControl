# Project Title

I am implementing various vehicle controllers for longitudinal and lateral vehicle control based on CARLA and the framework developed for University of Toronto's Intro to Self Driving Car course taught on coursera.
Here, I will implement and test the controllers and also list my analysis of each controller

## Getting Started

1. Clone this repo
2. Coming soon

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

## Lateral controllers

### Pure Pursuit Controller

This is the geometric controller using lookahead distance and is used to reduce cross-track (lateral) error.

Let's review its performance under different gain values

1. __*small* k__
  * More accurately tracks *curved* paths
  * *oscillating* on discontinuous track (e.g., lane change)
  Here you can see the car oscillating during a lane change for a very small *k = 0.2*
    * This happens as the controller is better suited to tracking curved paths as it is assumed in its derivation.

  ![Oscillating Pure Pursuit](/img/pp_k_small.gif)


2. __*large* k__
  * Less accurately tracks curved paths
  * *smooth* on discontinuous track (e.g., lane change)

  ![Oscillating Pure Pursuit](/img/pp_k_big.gif)

#### PERFORMANCE

| Path         | Small k                                      | Large k                                                    |
|--------------|----------------------------------------------|------------------------------------------------------------|
| Discontinous | <span style="color:red">Oscillatory</span>   :thumbsdown:                                | <span style="color:green">Smooth :thumbsup:</span>                                                    |
| Curved       | <span style="color:green">Smooth :thumbsup:</span>                                       | <span style="color:red">Oscillatory</span> :thumbsdown:                                               |
| Tracking Accuracy | :heavy_check_mark: | :heavy_multiplication_x: |
| Stability        | :heavy_multiplication_x: | :heavy_check_mark: |
| Reason       | Better tracks curved paths as per derivation | Large k leads to frequent steering changes for curved path |

<!--
Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->
