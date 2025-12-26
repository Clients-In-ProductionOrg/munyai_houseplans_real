import HousePlanCard from "./HousePlanCard";
import houseMadison from "@/assets/house-madison.jpg";
import houseOakwood from "@/assets/house-oakwood.jpg";
import houseSummit from "@/assets/house-summit.jpg";

const PopularPlans = () => {
  const plans = [
    {
      image: houseMadison,
      title: "The Madison",
      beds: 3,
      baths: 2,
      sqft: "2,150",
      price: "1,299"
    },
    {
      image: houseOakwood,
      title: "The Oakwood",
      beds: 4,
      baths: 3,
      sqft: "2,850",
      price: "1,599"
    },
    {
      image: houseSummit,
      title: "The Summit",
      beds: 5,
      baths: 4,
      sqft: "3,200",
      price: "2,299"
    }
  ];

  return (
    <section id="plans" className="py-20 bg-background">
      <div className="container">
        <div className="text-center space-y-4 mb-12 animate-fade-in">
          <h2 className="text-4xl font-bold text-foreground">Popular House Plans</h2>
          <p className="text-lg text-muted-foreground">
            Trending designs chosen by thousands of homeowners
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {plans.map((plan, index) => (
            <HousePlanCard key={index} {...plan} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default PopularPlans;
