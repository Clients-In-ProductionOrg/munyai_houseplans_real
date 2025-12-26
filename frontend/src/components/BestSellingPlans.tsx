import HousePlanCard from "./HousePlanCard";
import houseCraftsman from "@/assets/house-craftsman.jpg";
import houseColonial from "@/assets/house-colonial.jpg";
import houseRanch from "@/assets/house-ranch.jpg";
import houseContemporary from "@/assets/house-contemporary.jpg";

const BestSellingPlans = () => {
  const plans = [
    {
      image: houseCraftsman,
      title: "The Craftsman",
      beds: 3,
      baths: 2,
      sqft: "1,850",
      price: "999",
      isBestseller: true
    },
    {
      image: houseColonial,
      title: "The Colonial",
      beds: 4,
      baths: 3,
      sqft: "2,400",
      price: "1,399",
      isBestseller: true
    },
    {
      image: houseRanch,
      title: "The Ranch",
      beds: 3,
      baths: 2,
      sqft: "1,650",
      price: "899",
      isBestseller: true
    },
    {
      image: houseContemporary,
      title: "The Contemporary",
      beds: 4,
      baths: 3,
      sqft: "2,650",
      price: "1,699",
      isBestseller: true
    }
  ];

  return (
    <section id="styles" className="py-20 bg-muted/30">
      <div className="container">
        <div className="text-center space-y-4 mb-12 animate-fade-in">
          <h2 className="text-4xl font-bold text-foreground">Best-Selling Designs</h2>
          <p className="text-lg text-muted-foreground">
            Our most loved house plans by customers nationwide
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {plans.map((plan, index) => (
            <HousePlanCard key={index} {...plan} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default BestSellingPlans;
